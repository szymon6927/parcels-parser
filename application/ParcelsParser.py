import pandas as pd

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
            print("Error: File not found or inccorect filename")
