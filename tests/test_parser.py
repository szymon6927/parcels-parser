import os
import unittest
import pandas as pd
from application.ParcelsParser import ParcelsParser


class TestPracelsParser(unittest.TestCase):

    def setUp(self):
        self.parser = ParcelsParser("./test_cadastral_parcels.tsv", "cadastral_parcel_identifier")

    def test_if_file_exist(self):
        file_path = self.parser.get_file()

        self.assertTrue(file_path, os.path.isfile(file_path))

    def test_if_file_doesnt_exist(self):
        self.parser.set_file("./test_cadastral_parcels_wrong.tsv")
        file_path = file_path = self.parser.get_file()

        self.assertTrue(file_path, os.path.isfile(file_path))

    def test_if_column_exist(self):
        dirpath = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(dirpath, self.parser.get_file())
        df = pd.read_csv(filepath, sep='\t')

        self.assertTrue(True, self.parser.get_column_name() in df.columns)


if __name__ == '__main__':
    unittest.main()
