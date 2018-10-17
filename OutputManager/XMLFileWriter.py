from OutputManager import FileWriter
from lxml import etree
import json

class XMLFileWriter(FileWriter.FileWriter):

    def write(self, data):
        root = etree.Element('QueryResults')
        elemtree = etree.ElementTree(root)

        for queryResult in data:
            queryElem = etree.SubElement(root, 'Query')
            for row in queryResult['Query Result']:
                rowElem = etree.SubElement(queryElem, 'Row')
                for i, field in enumerate(row):
                    fieldElem = etree.SubElement(rowElem, queryResult['Column Names'][i])
                    fieldElem.text = str(field)

        with open("./OutputFiles/XML/Output.xml", "wb") as outputFile:
            elemtree.write(outputFile)
