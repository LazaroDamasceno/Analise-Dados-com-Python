import polars as pl

def find_outliers_polars(df, column):
    Q1 = df.select(pl.col(column).quantile(0.25)).item()
    Q3 = df.select(pl.col(column).quantile(0.75)).item()
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_expression = (pl.col(column) < lower_bound) | (pl.col(column) > upper_bound)
    return df.select(outliers_expression).to_series().any()

def find_outliers_pandas(df, column):
    series = df[column]
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (series < lower_bound) | (series > upper_bound)
