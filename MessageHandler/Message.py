import json
from collections import namedtuple


class Message:

    def __init__(self):
        self.dbName = ''
        self.input = ''
        self.output = ''

    def initParams(self, dbName, input, output):
        self.dbName = dbName
        self.input = input
        self.output = output
        return self

    def initFromJson(self, string):
        msgJson = json.loads(string, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.dbName = msgJson.dbName
        self.input = msgJson.input
        self.output = msgJson.output
        return self


    def toJson(self):
        return json.dumps(self.__dict__)