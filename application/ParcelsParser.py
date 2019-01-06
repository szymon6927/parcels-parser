import pandas as pd
import re


class ParcelsParser():
    def __init__(self, file, column_name):
        """
        :param file: name of file with data
        :param column_name: name of column where data are located
        """
        self.file = file
        self.column_name = column_name
        self.data = []
        self.result = []

    def __repr__(self):
        return """
        Recruitment task
        Author: Szymon Miks
        miks.szymon@gmail.com
        04.01.2019
        Company: ADGROUP
        """

    def get_file(self):
        return self.file

    def get_column_name(self):
        return self.column_name

    def get_data(self):
        return self.data

    def get_result(self):
        return self.result

    def set_file(self, file):
        self.file = file

    def set_column_name(self, column_name):
        self.column_name = column_name

    def get_identifiers_data(self):
        """Get values form cadastral_parcel_identifier column
        and save it to self.data.
        Before this check if file and column exists.
        """
        try:
            df = pd.read_csv(self.file, sep='\t')
            if self.column_name in df.columns:
                identifiers_list = df[self.column_name].tolist()
                self.data = identifiers_list
            else:
                raise KeyError("cadastral_parcel_identifier not in file")
        except FileNotFoundError:
            print("Error: File not found or incorrect filename")

    def get_province_county_commune(self, segment):
        """Eg. segment = 101010, is separeted into three smaller two digit chunks
        :param segment: string with digit only
        :return: extracted values like province_code, county_code, commune_code from param
        """
        province_code = segment[:2]
        county_code = segment[2:4].replace('O', '0').lstrip("0")
        commune_code = segment[4:6].lstrip("0")  # remove leading

        return province_code, county_code, commune_code

    def extract_data(self):
        """Extract values with regex usage and helper function
        and save it to temporary dict
        then append dict to self.result
        """
        for identifiers in self.data:
            temp = {}
            first_segment = re.search('\d(.*?)(?=\-|\_)', identifiers).group(0)

            province_code, county_code, commune_code = self.get_province_county_commune(first_segment)
            comunne_type = re.search('(?<=\_|\-)(.*?)(?=\.|\,)', identifiers).group(0)
            district_number = re.search('(?<=\.|\,)(.*?)(?=\.)', identifiers).group(0).replace('0', '')
            parcel_number = re.search('(?!.*\.).+', identifiers).group(0).replace('\\', '/').replace('//', '/')

            temp['province_code'] = province_code
            temp['county_code'] = county_code
            temp['commune_code'] = commune_code
            temp['commune_type'] = comunne_type
            temp['district_number'] = district_number
            temp['parcel_number'] = parcel_number
            self.result.append(temp)

    def print_result(self):
        [print(f'For ID "{item_data}" extracted data is: \n {item_result} \n')
         for item_data, item_result in zip(self.data, self.result)]

    def beautify_print(self):
        for item_data, item_result in zip(self.data, self.result):
            print(f'For ID: {item_data} \n')
            print("Extracted data:")
            [print(f'{key}: {value}') for key, value in item_result.items()]

            divider = ''.join('-' for _ in range(80))
            print(divider)
