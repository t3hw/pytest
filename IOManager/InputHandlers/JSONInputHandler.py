from IOManager import IO
import json


class JSONInputHandler(IO.IO):

    def getResults(self, dataSource):
        jsonstr = None

        try:
            with open('./InputFiles/' + dataSource + '.json', 'r') as file:
                inputFile = file.read()
                jsonstr = json.loads(inputFile)
        except Exception as e:
            print('Error reading JSON file')
            print(e)

        return jsonstr
