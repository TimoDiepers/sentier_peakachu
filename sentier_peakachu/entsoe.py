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
