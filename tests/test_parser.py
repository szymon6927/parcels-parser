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

    def test_get_identifiers_data(self):
        dirpath = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(dirpath, self.parser.get_file())

        self.parser.set_file(filepath)
        self.parser.get_identifiers_data()
        data = self.parser.get_data()

        self.assertTrue(7, len(data))

    def test_province_county_commune(self):
        segment = "301304"
        province_code, county_code, commune_code = self.parser.get_province_county_commune(segment)

        self.assertEqual(province_code, "30")
        self.assertEqual(county_code, "13")
        self.assertEqual(commune_code, "4")

    def test_extract_data(self):
        dirpath = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(dirpath, self.parser.get_file())
        df = pd.read_csv(filepath, sep='\t')

        self.parser.set_file(filepath)
        self.parser.get_identifiers_data()
        self.parser.extract_data()
        result = self.parser.get_result()

        province_code_list = df['province_code'].astype(str).tolist()
        county_code_list = df['county_code'].astype(str).tolist()
        commune_code_list = df['commune_code'].astype(str).tolist()
        commune_type_list = df['commune_type'].astype(str).tolist()
        district_number_list = df['district_number'].astype(str).tolist()
        parcel_number_list = df['parcel_number'].astype(str).tolist()

        for i, item in enumerate(result):
            self.assertEqual(item['province_code'], province_code_list[i])
            self.assertEqual(item['county_code'], county_code_list[i])
            self.assertEqual(item['commune_code'], commune_code_list[i])
            self.assertEqual(item['commune_type'], commune_type_list[i])
            self.assertEqual(item['district_number'], district_number_list[i])
            self.assertEqual(item['parcel_number'], parcel_number_list[i])


if __name__ == '__main__':
    unittest.main()
