import json
from collections import namedtuple


class Message:

    def __init__(self):
        self.dbName = ''
        self.fileType = ''

    def initParams(self, dbName, fileType):
        self.dbName = dbName
        self.fileType = fileType
        return self

    def initFromJson(self, string):
        msgJson = json.loads(string, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.dbName = msgJson.dbName
        self.fileType = msgJson.fileType
        return self


    def toJson(self):
        return json.dumps(self.__dict__)