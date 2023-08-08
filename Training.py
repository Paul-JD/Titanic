from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pandas import DataFrame
import pandas

# Data set imports

Training: DataFrame = pandas.read_csv('Csv_clean_files/Train_clean.csv', sep=',')
Training_Y: DataFrame = pandas.read_csv('Csv_clean_files/Train_result.csv', sep=',')
Dev: DataFrame = pandas.read_csv('Csv_clean_files/Dev_clean.csv', sep=',')
Dev_Y: DataFrame = pandas.read_csv('Csv_clean_files/Dev_result.csv', sep=',')

# Splitting Training

train_X, test_X, train_Y, test_Y = train_test_split(Training, Training_Y, train_size=0.8, random_state=42)

print('stop')
