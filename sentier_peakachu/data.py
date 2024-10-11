import warnings
from datetime import datetime

import pandas as pd
import sentier_data_tools as sdt

from sentier_peakachu.entsoe import get_generation_data
from sentier_peakachu.iri_mapping import (
    DIRTY_BONSAI_PRODUCT_IRIS_MAPPING,
    DIRTY_TRACE_AGGREGATION,
    ENTSOE_PRODUCT_IRIS_MAPPING,
    TRACE_PRODUCT_IRIS_MAPPING,
)
from sentier_peakachu.utils_location import get_geonames_iri_from_iso_code


def create_local_electricity_datastorage(reset: bool = True):
    if reset:
        sdt.reset_local_database()
    start_time = pd.Timestamp("20221008", tz="Europe/Brussels")
    end_time = pd.Timestamp("20221009", tz="Europe/Brussels")
    create_country_mix_dataset("DE", start_time, end_time)

    create_plant_emission_datasets()
    create_bonsai_emission_factor_datasets()


def create_country_mix_dataset(
    country_code: str, start_time: pd.Timestamp, end_time: pd.Timestamp
):
    # DF1

    metadata = sdt.Datapackage(
        name="electricity_markets",
        description="Electricity markets data from ENTSO-E",
        contributors=[
            {
                "title": "Peakachu",
                "path": "https://github.com/TimoDiepers/sentier_peakachu/",
                "role": "author",
            },
        ],
        homepage="https://github.com/TimoDiepers/sentier_peakachu/",
    ).metadata()

    df = get_generation_data(
        country_code=country_code,
        start=start_time,
        end=end_time,
    )
    df.index.name = "https://vocab.sentier.dev/units/quantity-kind/Time"
    df = df.reset_index()

    df = df.rename(columns=ENTSOE_PRODUCT_IRIS_MAPPING)

    units_tech = ["https://vocab.sentier.dev/units/unit/MegaW-HR"] * len(
        ENTSOE_PRODUCT_IRIS_MAPPING
    )  # MW not Mwh but no entry in SKOSMOS
    units_time = [
        "https://vocab.sentier.dev/units/unit/SEC",
    ]

    UNITS = units_time + units_tech

    sdt.Dataset(
        name="electricity mixes",
        dataframe=df,
        kind=sdt.DatasetKind.BOM,
        product="http://openenergy-platform.org/ontology/oeo/OEO_00000139",
        columns=[{"iri": x, "unit": y} for x, y in zip(df.columns, UNITS)],
        metadata=metadata,
        location=get_geonames_iri_from_iso_code(country_code),
        version=1,
        valid_from=datetime(2018, 1, 1),
        valid_to=datetime(2028, 1, 1),
    ).save()


def create_plant_emission_datasets():
    # DF2
    metadata = sdt.Datapackage(
        name="emission data power plants",
        description="Climate trace emission data for power plants",
        contributors=[
            {
                "title": "Peakachu",
                "path": "https://github.com/TimoDiepers/sentier_peakachu/",
                "role": "author",
            },
        ],
        homepage="https://github.com/TimoDiepers/sentier_peakachu/",
    ).metadata()

    COLUMNS_POWERPLANTS = [
        "https://example.com/model-terms/identifier",  # to be added to SKOSMOS model terms
        "https://example.com/model-terms/name",  # to be added to SKOSMOS model terms
        "https://example.com/model-terms/start_time",  # to be added to SKOSMOS model terms
        "https://example.com/model-terms/end_time",  # to be added to SKOSMOS model terms
        "https://example.com/process-terms/powergeneration",  # to be added to SKOSMOS process terms
        "http://openenergy-platform.org/ontology/oeo/OEO_00260007",  # CO2 emission
    ]

    UNITS_POWERPLANTS = [
        "https://example.com/model-terms/integer",  # to be added to SKOSMOS model terms
        "https://example.com/model-terms/name",  # to be added to SKOSMOS model terms
        "https://vocab.sentier.dev/units/unit/SEC",
        "https://vocab.sentier.dev/units/unit/SEC",
        "https://vocab.sentier.dev/units/unit/MegaW-HR",
        "https://vocab.sentier.dev/units/unit/TON_Metric",
    ]

    trace_frame = pd.read_csv("../data/electricity-generation_emissions_sources.csv")

    filtered_df = trace_frame[trace_frame["gas"] == "co2e_100yr"]
    grouped_dfs = {
        name: group
        for name, group in filtered_df.groupby(["iso3_country", "source_type"])
    }

    for (country, source_type), df in grouped_dfs.items():
        if source_type not in TRACE_PRODUCT_IRIS_MAPPING.keys():
            warnings.warn(
                f"Source type {source_type} not found, skipping Dataset creation"
            )
            continue

        geonames_iri = get_geonames_iri_from_iso_code(country)
        if not geonames_iri:
            warnings.warn(
                f"Location not found for {country}, skipping Dataset creation"
            )
            continue
        filtered_df = df[
            [
                "source_id",
                "source_name",
                "start_time",
                "end_time",
                "activity",
                "emissions_quantity",
            ]
        ]
        filtered_df.columns = COLUMNS_POWERPLANTS
        valid_from_str = min(df["start_time"])
        valid_to_str = max(df["end_time"])

        sdt.Dataset(
            name=f"power plant data, {country}, {source_type}",
            dataframe=filtered_df,
            kind=sdt.DatasetKind.BOM,
            product=TRACE_PRODUCT_IRIS_MAPPING[source_type],
            columns=[
                {"iri": x, "unit": y} for x, y in zip(df.columns, UNITS_POWERPLANTS)
            ],
            metadata=metadata,
            location=geonames_iri,
            version=1,
            valid_from=datetime.strptime(valid_from_str, "%Y-%m-%d %H:%M:%S"),
            valid_to=datetime.strptime(valid_to_str, "%Y-%m-%d %H:%M:%S"),
        ).save()


def create_bonsai_emission_factor_datasets():
    """
    Create datasets for emission factors for different sources of electricity from the bonsai database,
    splitting emissions in direct and indirect emissions.
    Unit is kg CO2-eq/kWh.
    """

    metadata = sdt.Datapackage(
        name="emission factors for regional electricity producing technologies",
        description="Bonsai emission factor data for regional electricity producing technologies",
        contributors=[
            {
                "title": "Karin Treyer",
                "path": "https://www.psi.ch/en/ta/people/karin-treyer",
                "role": "author",
            },
            {
                "title": "Chris Mutel",
                "path": "https://chris.mutel.org/",
                "role": "wrangler",
            },
        ],
        homepage="https://example.com/additional_inventories",
    ).metadata()

    UNITS_EMISSION_FACTORS = [
        "https://example.com/units/kgCO2eqPerkWh",
        "https://example.com/units/kgCO2eqPerkWh",
    ]
    COLUMNS_EMISSION_FACTORS = [
        "https://example.com/direct_CO2_emissions",
        "https://example.com/indirect_CO2_emissions",
    ]

    bonsai_frame = pd.read_csv("../data/bonsai_emission_factors.csv", delimiter=";")

    filtered_df = bonsai_frame[
        [
            "description",
            "region_code",
            "direct emission factor",
            "indirect emission factor",
        ]
    ]

    grouped_dfs = {
        name: group
        for name, group in filtered_df.groupby(["region_code", "description"])
    }

    for (country, technology), df in grouped_dfs.items():
        geonames_iri = get_geonames_iri_from_iso_code(country)
        if not geonames_iri:
            warnings.warn(
                f"Location not found for {country}, skipping Dataset creation"
            )
            continue
        technology_iri = DIRTY_BONSAI_PRODUCT_IRIS_MAPPING.get(technology)
        if not technology_iri:
            warnings.warn(
                f"Technology {technology} not found, skipping Dataset creation"
            )
            continue
        df = df[["direct emission factor", "indirect emission factor"]]
        df.columns = COLUMNS_EMISSION_FACTORS
        valid_from_str = "2016-01-01"  # Bonsai/EXIOBASE data from year 2016
        valid_to_str = "2024-12-31"

        sdt.Dataset(
            name=f"bonsai emission factors, {country}, {technology}",
            dataframe=df,
            kind=sdt.DatasetKind.BOM,
            product=technology_iri,
            columns=[
                {"iri": x, "unit": y}
                for x, y in zip(df.columns, UNITS_EMISSION_FACTORS)
            ],
            metadata=metadata,
            location=geonames_iri,
            version=1,
            valid_from=valid_from_str,
            valid_to=valid_to_str,
        ).save()
