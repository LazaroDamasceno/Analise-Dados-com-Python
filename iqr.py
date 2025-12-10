import polars as pl
import pandas as pd

def find_outliers_polars(df: pl.DataFrame, column: str | int | float) -> pl.DataFrame:
    Q1 = df.select(pl.col(column).quantile(0.25).alias("Q1")).item()
    Q3 = df.select(pl.col(column).quantile(0.75).alias("Q3")).item()
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df.with_columns(
        is_outlier=(
            (pl.col(column) < lower_bound) | (pl.col(column) > upper_bound)
        )
    )
    return df

def find_outliers_pandas(df: pd.DataFrame, column: str | int | float) -> pd.DataFrame:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    is_outlier = (df[column] < lower_bound) | (df[column] > upper_bound)
    df['is_outlier'] = is_outlier
    return df