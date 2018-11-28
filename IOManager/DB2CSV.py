from IOManager import IO


class DB2CSV(IO.IO):

    def getResults(self, connection):
        return self.getDataFromDB(connection)

    def write(self, data):
        self.writeCSV(data)
