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
