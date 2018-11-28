from IOManager.InputHandlers import DBInputHandler, JSONInputHandler
from IOManager.OutputHandlers import XMLOutputHandler, DBOutputHandler, JSONOutputHandler, CSVOutputHandler


class IOFactory:

    @staticmethod
    def getDBInputHandler():
        return DBInputHandler.DBInputHandler()

    @staticmethod
    def getJSONInputHandler():
        return JSONInputHandler.JSONInputHandler()

    @staticmethod
    def getCSVOutputHandler():
        return CSVOutputHandler.CSVOutputHandler()

    @staticmethod
    def getXMLOutputHandler():
        return XMLOutputHandler.XMLOutputHandler()

    @staticmethod
    def getJSONOutputHandler():
        return JSONOutputHandler.JSONOutputHandler()

    @staticmethod
    def getDBOutputHandler():
        return DBOutputHandler.DBOutputHandler()

    @staticmethod
    def getInput(factoryType):
        switcher = {
            "DB":  IOFactory.getDBInputHandler(),
            "JSON": IOFactory.getJSONInputHandler()
        }

        return switcher.get(factoryType)

    @staticmethod
    def getOutput(factoryType):
        switcher = {
            "CSV":  IOFactory.getCSVOutputHandler(),
            "XML":  IOFactory.getXMLOutputHandler(),
            "JSON": IOFactory.getJSONOutputHandler(),
            "DB":   IOFactory.getDBOutputHandler()
        }

        return switcher.get(factoryType)