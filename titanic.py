import pandas as pd

Train_result = pd.read_csv('Csv_files/gender_submission.csv', sep=',')
Train = pd.read_csv('Csv_files/train.csv', sep=',')
Test = pd.read_csv('Csv_files/test.csv', sep=',')
