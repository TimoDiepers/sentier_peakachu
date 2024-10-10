from datetime import datetime

import pandas as pd


def filter_timespan(
    df: pd.DataFrame, begin_date: datetime, end_date: datetime
) -> pd.DataFrame:
    return df[
        (
            df["https://example.com/units/start_time"]
            <= begin_date.strftime("%Y-%m-%d %H:%M:%S")
        )
        & (
            df["https://example.com/units/end_time"]
            >= end_date.strftime("%Y-%m-%d %H:%M:%S")
        )
    ]
