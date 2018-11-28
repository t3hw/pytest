from IOManager import IOFactory


class IncomingMessageHandler:
    def HandleMessage(self, connection, input, output):
        inputHandler = IOFactory.IOFactory.getInput(input)
        outputHandler = IOFactory.IOFactory.getOutput(output)
        results = None

        try:
            results = inputHandler.getResults(connection)
        except Exception as e:
            print('Error reading data')
            print(e)

        try:
            outputHandler.write(results)
        except Exception as e:
            print('Error saving output')
            print(e)
