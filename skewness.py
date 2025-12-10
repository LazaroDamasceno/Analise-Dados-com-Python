import polars as pl

def is_right_skewed_polars(df, column):
    skew = df.select(pl.col(column).skew()).item()
    has_zeroes_or_negatives = df.filter(pl.col(column) <= 0.0).height > 0
    if (skew > 1 and has_zeroes_or_negatives): 
        print(f'Para {column}: Use np.log1p().')
    elif (skew > 1 and not has_zeroes_or_negatives): 
        print(f'Para {column}: Use np.log().')