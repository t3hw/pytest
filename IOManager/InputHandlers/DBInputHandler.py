from IOManager import IO
from DB import DBManager


class DBInputHandler(IO.IO):

    def getResults(self, dataSource):
        dbm = DBManager.DBManager

        connection = dbm.getConnection(dataSource)

        results = None

        try:
            results = dbm.executeAllQueries(connection)
        except Exception as e:
            print('Error executing queries')
            print(e)

        return results
