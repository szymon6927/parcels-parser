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
