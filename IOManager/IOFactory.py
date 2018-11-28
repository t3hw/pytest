from IOManager import DB2CSV, DB2XML, DB2JSON, DB2DB, JSON2DB



class IOFactory:

    @staticmethod
    def getDB2CSV():
        return DB2CSV.DB2CSV()

    @staticmethod
    def getDB2XML():
        return DB2XML.DB2XML()

    @staticmethod
    def getDB2JSON():
        return DB2JSON.DB2JSON()

    @staticmethod
    def getDB2DB():
        return DB2DB.DB2DB()

    @staticmethod
    def getJSON2DB():
        return JSON2DB.JSON2DB()

    @staticmethod
    def getIO(factoryType):
        switcher = {
            "DB2CSV":  IOFactory.getDB2CSV(),
            "DB2XML":  IOFactory.getDB2XML(),
            "DB2JSON": IOFactory.getDB2JSON(),
            "DB2DB":   IOFactory.getDB2DB(),
            "JSON2DB": IOFactory.getJSON2DB()
        }

        return switcher.get(factoryType)
