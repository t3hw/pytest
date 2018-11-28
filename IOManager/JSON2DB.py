from IOManager import IO


class JSON2DB(IO.IO):

    def getResults(self, connection):
        return self.getJsonFromFile(connection)

    def write(self, data):
        self.writeDB(data)
