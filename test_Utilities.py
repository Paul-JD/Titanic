from unittest import TestCase
from Utilities import import_file
from pandas import DataFrame


class TestFile(TestCase):

    def test_import_file(self):
        self.assertEqual(type(import_file('Csv_files/train.csv')), DataFrame)
        self.assertEqual(import_file('test/test.csv'), FileNotFoundError)
