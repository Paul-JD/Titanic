# Packages import

import pandas as pd
from pandas import DataFrame

# Data set imports

Train: DataFrame = pd.read_csv('Csv_files/train.csv', sep=',')
Test: DataFrame = pd.read_csv('Csv_files/test.csv', sep=',')
Test_result: DataFrame = pd.read_csv('Csv_files/gender_submission.csv', sep=',')

# Separation of Train result and Train data set

Train_result = Train['Survived']
Train = Train._drop_axis(labels='Survived', axis=1)

# Drop Cabin Label because to many NA

Train = Train._drop_axis(labels="Cabin", axis=1)
Test = Test._drop_axis(labels="Cabin", axis=1)

# Remove NA from Ages columns

Train['Age'] = Train['Age'].fillna(-1)
Test['Age'] = Test['Age'].fillna(-1)

# Drop Na if still some

Train = Train.dropna()
Test = Test.dropna()

# Check NA values

check_null_values_Train = Train.isnull().sum()
check_null_values_Test = Test.isnull().sum()

print(check_null_values_Train)
print(Train.shape)
print(check_null_values_Test)
print(Test.shape)
