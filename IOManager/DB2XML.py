from IOManager import IO


class DB2XML(IO.IO):

    def getResults(self, connection):
        return self.getDataFromDB(connection)

    def write(self, data):
        self.writeXML(data)
