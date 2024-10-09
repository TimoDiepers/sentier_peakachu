from datetime import datetime

import pandas as pd
import sentier_data_tools as sdt
from loguru import logger

from sentier_peakachu.entsoe import get_generation_data


def create_local_datastorage(reset: bool = True):
    if reset:
        sdt.reset_local_database()
    create_market_datapackage()
    create_powerplant_datapackage()
    
def create_market_datapackage():
    metadata_markets = sdt.Datapackage(
        name="electricity_markets",
        description="Electricity markets blabla",
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
        country_code=COUNTRY,
        start=pd.Timestamp("20241008", tz="Europe/Brussels"),
        end=pd.Timestamp("20241009", tz="Europe/Brussels"),
    )
    df.index.name = "timestamp"
    df = df[["Fossil Brown coal/Lignite", "Fossil Gas", "Solar"]].reset_index()
    df.columns = ["timestamp", "https://example.com/coal", "https://example.com/gas", "https://example.com/pv"]
    
    sdt.Dataset(
        name=f"electricity mixes",
        data=df,
        kind=sdt.DatasetKind.BOM,
        product="http://openenergy-platform.org/ontology/oeo/OEO_00000139",
        columns=[{"iri": x, "unit": y} for x, y in zip(df.columns, UNITS_MARKETS)],
        metadata=metadata_markets,
        location=f"https://example.com/locations/{COUNTRY}",
        version=1,
        valid_from=datetime(2018, 1, 1),
        valid_to=datetime(2028, 1, 1),
    ).save()
    
def create_powerplant_datapackage():
    metadata_coal_power_plants = sdt.Datapackage(
        name="emission data coal power plants",
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

    df = create_powerplant_dummy()
    df['total_production_at_timestamp'] = df.groupby('timestamp')["https://example.com/Energy"].transform('sum')
    df['EF'] = df["https://example.com/GWP100"]/ df['total_production_at_timestamp']
    dataset_id = sdt.Dataset(
        name=f"power plant data",
        data=df,
        kind=sdt.DatasetKind.BOM,
        product="http://openenergy-platform.org/ontology/oeo/OEO_00000139",
        columns=[{"iri": x, "unit": y} for x, y in zip(df.columns, UNITS_COAL_PP)],
        metadata=metadata_coal_power_plants,
        location=f"https://example.com/locations/{COUNTRY}",
        version=1,
        valid_from=datetime(2018, 1, 1),
        valid_to=datetime(2028, 1, 1),
    ).save()

def create_powerplant_dummy():
    columns = ["timestamp", "powerplant_name", "https://example.com/Energy", "https://example.com/GWP100"]
    timestamp = [datetime(2020, 1, 1, 0, 0, 0), datetime(2020, 1, 1, 0, 0, 0), datetime(2020, 1, 1, 0, 0, 0), datetime(2021, 1, 1, 0, 0, 0), datetime(2021, 1, 1, 0, 0, 0), datetime(2021, 1, 1, 0, 0, 0)]

    powerplant_name = ["coal plant 1", "coal plant 2", "coal plant 3", "coal plant 1", "coal plant 2", "coal plant 3"] 
    production_vol = [100, 200, 300, 80, 210, 270]
    GWP = [50, 100, 150, 40, 110, 140]
    return pd.DataFrame(list(zip(timestamp, powerplant_name, production_vol, GWP)), columns=columns)

UNITS_MARKETS = ["https://example.com/units/datetime", "https://example.com/units/MW", "https://example.com/units/MW", "https://example.com/units/MW"]
UNITS_COAL_PP = ["https://example.com/units/datetime", "https://example.com/units/plant_name", "https://example.com/units/MWh", "https://example.com/units/MtCO2eq", "https://example.com/units/MtCO2eq/MWh"]
COUNTRY = "PL"
