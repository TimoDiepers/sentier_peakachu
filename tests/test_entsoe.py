import pandas as pd

from sentier_peakachu.entsoe import get_generation_data


def test_entsoe():
    query = {
        "country_code": "DE",
        "start": pd.Timestamp("20241008", tz="Europe/Brussels"),
        "end": pd.Timestamp("20241009", tz="Europe/Brussels"),
    }

    df = get_generation_data(**query)
    expected_df = pd.read_csv(
        "tests/data/entsoe_de_generation.csv", index_col=0, parse_dates=True
    )

    assert pd.testing.assert_frame_equal(df, expected_df)
