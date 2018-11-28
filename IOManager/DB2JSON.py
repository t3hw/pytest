import json
from IOManager import IO


class DB2JSON(IO.IO):

    def getResults(self, connection):
        return self.getDataFromDB(connection)

    def write(self, data):
        self.writeJson(data)
