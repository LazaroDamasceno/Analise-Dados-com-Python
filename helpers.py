import numpy as np
import pandas as pd

class SeriesTransformer:

    def __init__(self, series: pd.Series):
        self.series = series
        self.df = series.to_frame("value")

        q1 = self.series.quantile(0.25)
        q3 = self.series.quantile(0.75)
        iqr = q3 - q1
        self.lower_limit = q1 - 1.5 * iqr
        self.upper_limit = q3 + 1.5 * iqr

    def is_outlier(self, number: float) -> bool:
        return number < self.lower_limit or number > self.upper_limit

    def has_outliers(self) -> bool:
        return self.df["value"].apply(self.is_outlier).any()

    def transform(self) -> pd.Series:

        big_skew = self.series.skew() > 1
        any_zero = (self.df["value"] <= 0).any()
        any_outlier = self.has_outliers()

        if (big_skew or any_outlier) and not any_zero:
            return np.log(self.df["value"])
        elif (big_skew or any_outlier) and any_zero:
            return np.log1p(self.df["value"])
        else:
            return self.df["value"]
