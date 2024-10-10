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

        total_emissions = df["https://example.com/emissions"].sum()
        total_production = df["https://example.com/powergeneration"].sum()
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

        rounded_begin_date = pd.Timestamp(self.demand.begin_date).round("15min")
        rounded_end_date = pd.Timestamp(self.demand.end_date).round("15min")

        df_merged["https://example.com/timestamp"] = pd.to_datetime(
            df_merged["https://example.com/timestamp"]
        ).dt.tz_localize(None)
        filtered_df = df_merged[
            (df_merged["https://example.com/timestamp"] >= rounded_begin_date)
            & (df_merged["https://example.com/timestamp"] <= rounded_end_date)
        ]
        return filtered_df

    def calculate_market_mix(self, df_mixes: pd.DataFrame) -> pd.DataFrame:
        if df_mixes.empty:
            raise ValueError(f"Input DataFrame is empty.")
        average_mix = df_mixes.mean().drop("https://example.com/timestamp")
        return average_mix / average_mix.sum()

    def calculate_impact(self, market_shares: pd.Series) -> float:
        emission_factors = []
        for technology in market_shares.index:
            ef = self.calculate_technology_emission_factor(ProductIRI(technology))
            emission_factors.append(ef)
        logger.debug(f"Market shares: {market_shares}")
        logger.debug(f"Emission factors: {emission_factors}")
        return self.demand.amount * sum(market_shares * emission_factors)

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
