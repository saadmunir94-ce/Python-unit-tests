import pandas as pd
import numpy as np

# creating series 1
series1 = pd.Series([11, 0, 2, 43, 9, 27, np.nan, 10, np.nan])
#series1 = pd.Series([0, 0, 2, 0, 0, 2, 0, 0, 0])
# creating series 2
series2 = pd.Series([16, np.nan, 2, 23, 5, 40, 54, 2, 19])
# NaN replacement
replace_nan = 10
# calling and returning to result variable
result = series1.le(series2, fill_value=replace_nan)
print(result.all(axis=None))
df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})

df.set_index("year", inplace=True)
print(df)
print(df.le(df["sale"], axis=0).all(axis=None))
print("Last row name: {}".format(df.index[-1]))