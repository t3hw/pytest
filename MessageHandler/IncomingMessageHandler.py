from OutputManager import FWFactory
from DB import DBManager


class IncomingMessageHandler:
    def HandleMessage(self, msg):
        print('Recieved incoming message')
        print('DB Name: ' + msg.dbName)
        print('Output Type: ' + msg.fileType)

        dbm = DBManager.DBManager
        results = None
        try:
            results = dbm.executeAllQueries(msg.dbName)
        except Exception as e:
            print('Error executing queries')
            print(e)

        try:
            writer = FWFactory.FWFactory.getFW(msg.fileType)
            writer.write(results)
        except Exception as e:
            print('Error saving output')
            print(e)
