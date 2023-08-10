# Packages import

import pandas as pd
from pandas import DataFrame

# Data set imports

Train: DataFrame = pd.read_csv('Csv_files/train.csv', sep=',')
Test: DataFrame = pd.read_csv('Csv_files/test.csv', sep=',')
Test_result: DataFrame = pd.read_csv('Csv_files/gender_submission.csv', sep=',')

# Drop Cabin Label because to many NA

Train = Train._drop_axis(labels="Cabin", axis=1)
Test = Test._drop_axis(labels="Cabin", axis=1)

# Remove NA from Ages columns

Train['Age'] = Train['Age'].fillna(Train['Age'].median())
Test['Age'] = Test['Age'].fillna(Test['Age'].median())

# Remove NA from Embarked columns
Train['Embarked'] = Train['Embarked'].fillna('S')
Test['Embarked'] = Test['Embarked'].fillna('S')

# Remove NA from Fare Columns
Train["Fare"] = Train["Fare"].fillna(Train["Fare"].median())
Test["Fare"] = Test["Fare"].fillna(Test["Fare"].median())

# Remove NA from SibSP as 0

Train["SibSP"] = Train["SibSP"].fillna(0)
Test["SibSP"] = Test["SibSP"].fillna(0)

# Label Sex by 0 & 1

Train.loc[Train['Sex'] == 'male', 'Sex'] = 0
Test.loc[Test['Sex'] == 'female', 'Sex'] = 1

# Drop Na if still some

Train = Train.dropna()
Test = Test.dropna()

# Separation of Train result and Train data set

Train_result = Train['Survived']
Train = Train._drop_axis(labels='Survived', axis=1)

# Check NA values

check_null_values_Train = Train.isnull().sum()
check_null_values_Test = Test.isnull().sum()

print(check_null_values_Train)
print(check_null_values_Test)

# Save as Csv files
Train.to_csv('Csv_clean_files/Train_clean.csv', index=False)
Test.to_csv('Csv_clean_files/Dev_clean.csv', index=False)
Train_result.to_csv('Csv_clean_files/Train_result.csv', index=False)
Test_result.to_csv('Csv_clean_files/Dev_result.csv', index=False)

#
