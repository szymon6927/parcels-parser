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
