import json
from collections import namedtuple


class Message:

    def __init__(self):
        self.dbName = ''
        self.action = ''

    def initParams(self, dbName, action):
        self.dbName = dbName
        self.action = action
        return self

    def initFromJson(self, string):
        msgJson = json.loads(string, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.dbName = msgJson.dbName
        self.action = msgJson.action
        return self


    def toJson(self):
        return json.dumps(self.__dict__)