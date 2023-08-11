from unittest import TestCase
from Function_Bank.Check_data import check_import_file, check_nan, check_column_numbers, check_dataset_length
from pandas import DataFrame
import pandas as pd
import numpy as np


class TestDataSet(TestCase):
    dataframe_test_1: DataFrame = pd.DataFrame(np.array([[5, None, 5], [5, 5, 3], [9, 15, 3]]))
    dataframe_test_2: DataFrame = pd.DataFrame(np.array([[5, 4], [5, None]]))
    dataframe_test_3: DataFrame = pd.DataFrame(np.array([[5, 4, 3], [5, 8, 78]]))

    def test_import_file(self):
        self.assertEqual(type(check_import_file('../Csv_clean_files/Train_clean.csv')), DataFrame)
        self.assertEqual(check_import_file('test/test.csv'), FileNotFoundError)

    # Control test and train have the same numbers of columns
    def test_check_column_numbers(self):
        self.assertTrue(check_column_numbers(self.dataframe_test_1, self.dataframe_test_3))
        self.assertFalse(check_column_numbers(self.dataframe_test_1, self.dataframe_test_2))

    # Control there is no NA values in the set
    def test_check_na_values(self):
        self.assertFalse(check_nan(self.dataframe_test_1))
        self.assertFalse(check_nan(self.dataframe_test_2))
        self.assertTrue(check_nan(self.dataframe_test_3))

    # Control Sets and results have the same numbers of raws
    def test_length_dataset(self):
        self.assertFalse(check_dataset_length(self.dataframe_test_1, self.dataframe_test_2))
        self.assertTrue(check_dataset_length(self.dataframe_test_2, self.dataframe_test_3))
