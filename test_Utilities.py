from unittest import TestCase
from Utilities import import_file
from pandas import DataFrame


class TestDataSet(TestCase):

    def test_import_file(self):
        self.assertEqual(type(import_file('Csv_clean_files/Train_clean.csv')), DataFrame)
        self.assertEqual(import_file('test/test.csv'), FileNotFoundError)

    # Control test and train have the same numbers of columns
    def test_columns_number(self):
        self.fail()

    # Control there is no NA values in the set
    def test_check_na_values(self):
        self.fail()

    # Control Sets and results have the same numbers of raws
    def test_length_dataset(self):
        self.fail()

