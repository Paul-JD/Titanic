import pandas
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Data set imports

Training: DataFrame = pandas.read_csv('../Csv_clean_files/Train_clean.csv', sep=',')
Training_Y: DataFrame = pandas.read_csv('../Csv_clean_files/Train_result.csv', sep=',')
Dev: DataFrame = pandas.read_csv('../Csv_clean_files/Dev_clean.csv', sep=',')
Dev_Y: DataFrame = pandas.read_csv('../Csv_clean_files/Dev_result.csv', sep=',')

# Splitting Training

train_X, test_X, train_Y, test_Y = train_test_split(Training, Training_Y, train_size=0.8, random_state=42)

# Train a random forest classifier
rfc = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0)
rfc.fit(Training, Training_Y.values.ravel())

# Make predictions on the validation set
Dev_pred_val = rfc.predict(test_X)

# Evaluate the model using accuracy score
accuracy = accuracy_score(test_Y, Dev_pred_val)
print(f'Accuracy: {accuracy:.2f}')
