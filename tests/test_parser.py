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


if __name__ == '__main__':
    unittest.main()
