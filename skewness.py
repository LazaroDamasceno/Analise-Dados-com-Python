import polars as pl

def is_right_skewed_log(df, column):
    skew = df.select(pl.col(column).skew()).item()
    has_zeroes_or_negatives = df.filter(pl.col(column) <= 0.0).height > 0
    return skew > 1 and not has_zeroes_or_negatives

def is_right_skewed_log1p(df, column):
    skew = df.select(pl.col(column).skew()).item()
    has_zeroes_or_negatives = df.filter(pl.col(column) <= 0.0).height > 0
    return skew > 1 and has_zeroes_or_negatives