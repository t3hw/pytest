from OutputManager import CSVFileWriter, XMLFileWriter, JSONFileWriter, TableWriter



class FWFactory:

    @staticmethod
    def getCSVFW():
        return CSVFileWriter.CSVFileWriter()

    @staticmethod
    def getXMLFW():
        return XMLFileWriter.XMLFileWriter()

    @staticmethod
    def getJSONFW():
        return JSONFileWriter.JSONFileWriter()

    @staticmethod
    def getInsertBuilder():
        return TableWriter.TableWriter()

    @staticmethod
    def getFW(writerType):
        switcher = {
            "CSV":  FWFactory.getCSVFW(),
            "XML":  FWFactory.getXMLFW(),
            "JSON": FWFactory.getJSONFW(),
            "TABLE": FWFactory.getInsertBuilder()
        }

        return switcher.get(writerType)
