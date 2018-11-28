from IOManager import IO
import json


class JSONOutputHandler(IO.IO):

    def write(self, data):
        jsoned = json.dumps(data, indent=4)
        self.writeFile("./OutputFiles/JSON/Output.json", jsoned)
