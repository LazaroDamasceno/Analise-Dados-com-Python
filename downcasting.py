import polars as pl

def safe_downcast_int(series: pl.Series) -> pl.Series:
    min_val = series.min()
    max_val = series.max()
    
    if min_val >= -128 and max_val <= 127:
        return series.cast(pl.Int8)
    elif min_val >= -32768 and max_val <= 32767:
        return series.cast(pl.Int16)
    elif min_val >= -(2**31) and max_val <= (2**31 - 1):
        return series.cast(pl.Int32)
    return series