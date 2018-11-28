from IOManager import IO
import json


class JSONInputHandler(IO.IO):

    def getResults(self, connection):
        jsonstr = None

        try:
            with open('./InputFiles/Input.json', 'r') as file:
                inputFile = file.read()
                jsonstr = json.loads(inputFile)
        except Exception as e:
            print('Error reading JSON file')
            print(e)

        return jsonstr
