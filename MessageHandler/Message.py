import json
from collections import namedtuple


class Message:

    def __init__(self):
        self.dataSource = ''
        self.input = ''
        self.output = ''

    def initParams(self, dataSource, input, output):
        self.dataSource = dataSource
        self.input = input
        self.output = output
        return self

    def initFromJson(self, string):
        msgJson = json.loads(string, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.dataSource = msgJson.dataSource
        self.input = msgJson.input
        self.output = msgJson.output
        return self


    def toJson(self):
        return json.dumps(self.__dict__)