from IOManager import IO
from DB import DBManager


class DBInputHandler(IO.IO):

    def getResults(self, connection):
        dbm = DBManager.DBManager
        results = None

        try:
            results = dbm.executeAllQueries(connection)
        except Exception as e:
            print('Error executing queries')
            print(e)

        return results
