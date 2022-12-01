import pandas as pd
import numpy as np


def miss():
    # create DataFrame with some missing values
    df = pd.DataFrame({'a': [4, np.nan, np.nan, 7, 8, 12],
                       'b': [np.nan, 6, 8, 14, 29, np.nan],
                       'c': [11, 8, 10, 6, 6, np.nan]})

    # view DataFrame
    return df.isnull().sum().sum() / len(df) * 100
