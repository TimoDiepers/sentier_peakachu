import warnings
from datetime import datetime

import pandas as pd
import sentier_data_tools as sdt

from sentier_peakachu.entsoe import get_generation_data
from sentier_peakachu.utils_location import get_geonames_iri_from_iso_code


def create_local_electricity_datastorage(reset: bool = True):
    if reset:
        sdt.reset_local_database()
    start_time = pd.Timestamp("20221008", tz="Europe/Brussels")
    end_time = pd.Timestamp("20221009", tz="Europe/Brussels")
    create_country_mix_dataset("DE", start_time, end_time)
    create_country_mix_dataset("PL", start_time, end_time)

    create_plant_emission_datasets()


def create_country_mix_dataset(
    country_code: str, start_time: pd.Timestamp, end_time: pd.Timestamp
):
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
    df.index.name = "timestamp"
    df = df[["Fossil Brown coal/Lignite", "Fossil Gas"]].reset_index()
    df.columns = [
        "https://example.com/timestamp",
        "https://example.com/coa",
        "https://example.com/gas",
    ]

    UNITS = [
        "https://example.com/units/datetime",
        "https://example.com/units/MW",
        "https://example.com/units/MW",
    ]

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

    UNITS_POWERPLANTS = [
        "https://example.com/units/datetime",
        "https://example.com/units/datetime",
        "https://example.com/units/plant_name",
        "https://example.com/units/MWh",
        "https://example.com/units/ttCO2eq",
        "https://example.com/units/tCO2eqPerMWh",
    ]
    COLUMNS_POWERPLANTS = [
        "https://example.com/identifier",
        "https://example.com/name",
        "https://example.com/units/start_time",
        "https://example.com/units/end_time",
        "https://example.com/powergeneration",
        "https://example.com/emissions",
    ]

    trace_frame = pd.read_csv("../data/electricity-generation_emissions_sources.csv")

    filtered_df = trace_frame[trace_frame["gas"] == "co2e_100yr"]
    grouped_dfs = {
        name: group
        for name, group in filtered_df.groupby(["iso3_country", "source_type"])
    }

    for (country, source_type), df in grouped_dfs.items():
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
            product=get_electricity_iri(source_type),
            columns=[
                {"iri": x, "unit": y} for x, y in zip(df.columns, UNITS_POWERPLANTS)
            ],
            metadata=metadata,
            location=geonames_iri,
            version=1,
            valid_from=datetime.strptime(valid_from_str, "%Y-%m-%d %H:%M:%S"),
            valid_to=datetime.strptime(valid_to_str, "%Y-%m-%d %H:%M:%S"),
        ).save()


def get_electricity_iri(source_type):
    return f"https://example.com/{source_type[:3]}"
