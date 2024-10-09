import pandas as pd

from sentier_peakachu.entsoe import get_generation_data


def test_entsoe():
    query = {
        "country_code": "DE",
        "start": pd.Timestamp("20241008", tz="Europe/Brussels"),
        "end": pd.Timestamp("20241009", tz="Europe/Brussels"),
    }

    get_generation_data(**query)
