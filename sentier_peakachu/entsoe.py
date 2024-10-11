import os

import pandas as pd
from dotenv import load_dotenv
from entsoe import EntsoePandasClient


def get_api_key():
    """
    Getting the API key from the .env file.
    """
    load_dotenv()
    API_KEY = os.getenv("ENTSOE_API_KEY")
    return API_KEY


def filter_actual_aggregated(df):
    """
    Curates the generation data from ENTSO-E API to only include the actual aggregated generation
    data.
    """
    if df.columns.nlevels == 1:  # sometimes, consumption data is not available
        return df

    df_filtered = df.loc[:, df.columns.get_level_values(1) == "Actual Aggregated"]
    df_filtered.columns = df_filtered.columns.droplevel(1)
    return df_filtered


def get_generation_data(country_code: str, start: pd.Timestamp, end: pd.Timestamp):
    """
    Get generation data from ENTSO-E API for a specific country and time range.

    Parameters
    ----------
    country_code : str
        Country code (e.g. 'DE' for Germany).
    start : pd.Timestamp
        Start date and time.
    end : pd.Timestamp
        End date and time.

    Returns
    -------
    pd.DataFrame
        Generation data for the specified country and time range.
    """
    client = EntsoePandasClient(api_key=get_api_key())
    df = client.query_generation(country_code=country_code, start=start, end=end)
    return filter_actual_aggregated(df)


entsoe_product_iris_mapping = {
    "Fossil Oil": "https://vocab.sentier.dev/products/crude-oil",
    "Fossil Oil shale": "https://vocab.sentier.dev/products/oil-shale",
    "Fossil Gas": "https://vocab.sentier.dev/products/natural-gas",
    "Fossil Coal-derived gas": "https://vocab.sentier.dev/products/coalbed-gas",
    "Fossil Hard coal": "https://vocab.sentier.dev/products/hard-coal",
    "Fossil Brown coal/Lignite": "https://vocab.sentier.dev/products/lignite",
    "Fossil Peat": "https://vocab.sentier.dev/products/peat",
    "Wind Offshore": "https://vocab.sentier.dev/products/offshore",
    "Wind Onshore": "https://vocab.sentier.dev/products/onshore",
    "Hydro Water Reservoir": "https://vocab.sentier.dev/products/hydro-reservoirs",
    "Hydro Pumped Storage": "https://vocab.sentier.dev/products/pumped-storage",
    "Hydro Run-of-river and poundage": "https://vocab.sentier.dev/products/run-of-river",
    "Marine": "https://vocab.sentier.dev/products/marine",
    "Solar": "http://openenergyplatform.org/ontology/oeo/OEO_00010419/",
    "Geothermal": "https://vocab.sentier.dev/products/geothermal",
    "Biomass": "https://vocab.sentier.dev/products/biomass",
    "Other renewable": "https://vocab.sentier.dev/products/other-renewable-sources",
    "Nuclear": "http://openenergyplatform.org/ontology/oeo/OEO_00010417/",
    "Waste": "https://vocab.sentier.dev/products/waste",
    "Other": "https://vocab.sentier.dev/products/other",
}

trace_product_iris_mapping = {
    "oil": "https://vocab.sentier.dev/products/fossil-oil",
    "gas": "https://vocab.sentier.dev/products/fossil-gas",
    "other_fossil": "https://vocab.sentier.dev/products/peat",
    "coal": "https://vocab.sentier.dev/products/fossil-coal",
    "biomass": "https://vocab.sentier.dev/products/biomass",
    "waste": "https://vocab.sentier.dev/products/waste",
}
