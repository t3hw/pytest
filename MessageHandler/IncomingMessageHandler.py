from IOManager import IOFactory


class IncomingMessageHandler:
    def HandleMessage(self, connection, action):
        IOHandler = IOFactory.IOFactory.getIO(action)
        results = None

        try:
            results = IOHandler.getResults(connection)
        except Exception as e:
            print('Error reading data')
            print(e)

        try:
            IOHandler.write(results)
        except Exception as e:
            print('Error saving output')
            print(e)
