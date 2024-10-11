import warnings
from datetime import datetime

import pandas as pd
from loguru import logger
from sentier_data_tools import (
    Dataset,
    Demand,
    Flow,
    GeonamesIRI,
    ProductIRI,
    RunConfig,
    SentierModel,
    UnitIRI,
)

from sentier_peakachu.iri_mapping import (
    DIRTY_BONSAI_PRODUCT_IRIS_MAPPING,
    DIRTY_TRACE_AGGREGATION,
)

from .utils_time import filter_timespan


class TopModel(SentierModel):
    pass


class BottomModel(SentierModel):
    pass


class ElectricitySourceModel(BottomModel):
    provides = {
        ProductIRI("https://example.com/pv"): "pv",
        ProductIRI("https://example.com/coa"): "coal",
        ProductIRI("https://example.com/gas"): "gas",
    }
    aliases = {}

    def run(self, abbreviate_iris: bool = True) -> tuple[list[Demand], list[Flow]]:
        self.prepare()

    def prepare(self) -> None:
        self.get_model_data()
        self.data_validity_checks()
        self.resample()

    def get_model_data(self) -> pd.DataFrame:
        datasets = list(
            Dataset.select().where(
                (Dataset.product == self.demand.product_iri)
                & (Dataset.location == self.demand.spatial_context)
            )
        )
        if not datasets:
            raise ValueError(
                f"No plant emissions data available for {self.demand.product_iri} in {self.demand.spatial_context}."
            )
        df_merged = self.merge_datasets_to_dataframes(datasets)
        return filter_timespan(df_merged, self.demand.begin_date, self.demand.end_date)

    def calculate_average_source_emission_factor(
        self, df: pd.DataFrame
    ) -> pd.DataFrame:
        if df.empty:
            raise ValueError(f"Input DataFrame is empty.")

        if df.empty:
            raise ValueError(
                f"No data available for the specific time range between {self.demand.begin_date} and {self.demand.end_date}."
            )

        total_emissions = df[
            "http://openenergy-platform.org/ontology/oeo/OEO_00260007"
        ].sum()
        total_production = df["https://example.com/process-terms/powergeneration"].sum()
        return total_emissions / total_production


class ElectricityMixModel(TopModel):
    provides = {
        ProductIRI(
            "http://openenergy-platform.org/ontology/oeo/OEO_00000139"
        ): "electricity",
    }
    aliases = {}

    def run(self, abbreviate_iris: bool = True) -> tuple[list[Demand], list[Flow]]:
        self.prepare()

    def prepare(self) -> None:
        self.get_model_data()
        self.data_validity_checks()
        self.resample()

    def get_model_data(self) -> pd.DataFrame:
        datasets = list(
            Dataset.select().where(
                (Dataset.product == self.demand.product_iri)
                & (Dataset.location == self.demand.spatial_context)
            )
        )
        if not datasets:
            raise ValueError(
                f"No electricity mix data available for {self.demand.product_iri} in {self.demand.spatial_context}."
            )
        df_merged = self.merge_datasets_to_dataframes(datasets)
        # logger.debug(f"Electricity mix data before filtering: {df_merged}")
        rounded_begin_date = pd.Timestamp(self.demand.begin_date).round("15min")
        rounded_end_date = pd.Timestamp(self.demand.end_date).round("15min")

        df_merged["https://vocab.sentier.dev/units/quantity-kind/Time"] = (
            pd.to_datetime(
                df_merged["https://vocab.sentier.dev/units/quantity-kind/Time"]
            ).dt.tz_localize(None)
        )
        filtered_df = df_merged[
            (
                df_merged["https://vocab.sentier.dev/units/quantity-kind/Time"]
                >= rounded_begin_date
            )
            & (
                df_merged["https://vocab.sentier.dev/units/quantity-kind/Time"]
                <= rounded_end_date
            )
        ]
        return filtered_df

    def calculate_market_mix(self, df_mixes: pd.DataFrame) -> pd.DataFrame:
        if df_mixes.empty:
            raise ValueError(f"Input DataFrame is empty.")
        average_mix = df_mixes.mean().drop(
            "https://vocab.sentier.dev/units/quantity-kind/Time"
        )
        return average_mix / average_mix.sum()

    def calculate_impact(self, market_shares: pd.Series) -> float:
        emission_factors = []
        market_shares.index = market_shares.index.map(
            lambda x: DIRTY_TRACE_AGGREGATION.get(x, x)
        )  # aggregate specific technologies
        grouped_market_shares = market_shares.groupby(market_shares.index).sum()

        considered_technologies_in_market = []
        for technology in grouped_market_shares.index:
            if (
                technology in DIRTY_TRACE_AGGREGATION.values()
            ):  # fossile technologies form climate traxe
                ef = self.calculate_technology_emission_factor(ProductIRI(technology))
                emission_factors.append(ef)
                considered_technologies_in_market.append(technology)
            elif technology in DIRTY_BONSAI_PRODUCT_IRIS_MAPPING.values():
                ef = self.get_bonsai_emission_factor(technology)
                if ef is None:
                    continue
                emission_factors.append(ef)
                considered_technologies_in_market.append(technology)
            else:
                warnings.warn(f"No emission factor available for {technology}.")

        considered_market_shares = grouped_market_shares.loc[
            considered_technologies_in_market
        ]
        considered_market_shares_normalized = (
            considered_market_shares / considered_market_shares.sum()
        )

        logger.debug(f"Market shares: {considered_market_shares_normalized}")
        logger.debug(f"Emission factors: {emission_factors}")
        return self.demand.amount * sum(
            considered_market_shares_normalized * emission_factors
        )

    def get_bonsai_emission_factor(self, product_iri: ProductIRI) -> float:
        datasets = list(
            Dataset.select().where(
                (Dataset.product == product_iri)
                & (Dataset.location == self.demand.spatial_context)
            )
        )
        if len(datasets) == 0:
            return None
        if len(datasets) == 1:
            dataframe = datasets[0].dataframe
            total_emissions = sum(
                dataframe["https://example.com/direct_CO2_emissions"],
                dataframe["https://example.com/indirect_CO2_emissions"],
            )
        else:
            merged_df = self.merge_datasets_to_dataframes(datasets)
            total_emissions = sum(
                merged_df["https://example.com/direct_CO2_emissions"].mean(),
                merged_df["https://example.com/indirect_CO2_emissions"].mean(),
            )

        logger.debug(f"{product_iri}: {total_emissions} kgCO2eq/kWh")
        return float(total_emissions)

    def calculate_technology_emission_factor(self, product_iri: ProductIRI) -> float:
        demand = Demand(
            product_iri=product_iri,
            unit_iri=UnitIRI("https://vocab.sentier.dev/units/unit/KilowattHour"),
            amount=1,
            spatial_context=self.demand.spatial_context,
            begin_date=self.demand.begin_date,
            end_date=self.demand.end_date,
        )
        model = ElectricitySourceModel(demand=demand, run_config=RunConfig())
        plant_emissions = model.get_model_data()
        return model.calculate_average_source_emission_factor(plant_emissions)
