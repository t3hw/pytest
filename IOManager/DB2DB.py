from IOManager import IO


class DB2DB(IO.IO):

    def getResults(self, connection):
        return self.getDataFromDB(connection)

    def write(self, data):
        self.writeDB(data)
