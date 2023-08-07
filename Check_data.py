import pandas as pd
from pandas import DataFrame

Train: DataFrame = pd.read_csv('Csv_files/train.csv', sep=',')
Test: DataFrame = pd.read_csv('Csv_files/test.csv', sep=',')
Test_result: DataFrame = pd.read_csv('Csv_files/gender_submission.csv', sep=',')

check_null_values = Train.isnull().sum()

Train = Train._drop_axis(labels="Cabin", axis=1)

for idx in Train.index:
    if Train.Age[idx].isNan():
        Train.Age[idx] = -1

check_null_values_2 = Train.isnull().sum()

print(check_null_values_2)
