import json
from OutputManager import FileWriter


class JSONFileWriter(FileWriter.FileWriter):

    def write(self, data):
        jsoned = json.dumps(data, indent=4)

        super().write("./OutputFiles/JSON/Output.json", jsoned)
