from OutputManager import FWFactory
from DB import DBManager


class IncomingMessageHandler:
    def HandleMessage(self, connection, action):
        dbm = DBManager.DBManager
        results = None
        try:
            results = dbm.executeAllQueries(connection)
        except Exception as e:
            print('Error executing queries')
            print(e)

        try:
            writer = FWFactory.FWFactory.getFW(action)
            writer.write(results)
        except Exception as e:
            print('Error saving output')
            print(e)
