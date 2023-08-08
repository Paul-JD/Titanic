from typing import Type

import pandas as pd
from pandas import DataFrame


def import_file(path: str) -> DataFrame | Type[FileNotFoundError]:
    try:
        return pd.read_csv(path, sep=',')
    except FileNotFoundError:
        print('No file found')
        return FileNotFoundError


def check_nan(data: DataFrame) -> bool:
    columns_names = data.columns

    for name in columns_names:
        if data[name].isnull().sum() > 0:
            return False
    return True

