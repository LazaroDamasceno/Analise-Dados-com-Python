def is_outlier(data_frame, column, value_row):
    Q1 = data_frame.select(column).quantile(0.25).item()
    Q3 = data_frame.select(column).quantile(0.75).item()
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    value = data_frame[value_row, column] 
    result = (value < lower_bound) or (value > upper_bound)
    return result

