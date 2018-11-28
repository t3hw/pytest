import os, shutil
import json
import csv
from lxml import etree
from DB import InsertBuilder, DBManager
from collections import namedtuple

class IO:
    # Reading the data from DB input source
    def getDataFromDB(self, connection):
        dbm = DBManager.DBManager
        results = None

        try:
            results = dbm.executeAllQueries(connection)
        except Exception as e:
            print('Error executing queries')
            print(e)

        return results

    # Reading a JSON from a file input source
    def getJsonFromFile(self, DBconnection):
        jsonstr = None

        try:
            with open('./InputFiles/Input2.json', 'r') as file:
                inputFile = file.read()
                #jsonstr = json.loads(inputFile, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
                jsonstr = json.loads(inputFile)
        except Exception as e:
            print('Error reading JSON file')
            print(e)

        return jsonstr

    # Override this by IO child classes
    def getResults(self, dataSource):
        pass

    # Override this by IO chile classes
    def write(self, data):
        pass

    # General file write method
    def writeFile(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    # Write a JSON output file
    def writeJson(self, data):
        jsoned = json.dumps(data, indent=4)
        self.writeFile("./OutputFiles/JSON/Output.json", jsoned)

    # Write an XML output file
    def writeXML(self, data):
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

    # Write a CSV output file
    def writeCSV(self, data):

        # Clean the folder before writing the data
        folder = './OutputFiles/CSV'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(e)

        for query in data:
            with open('./OutputFiles/CSV/Query'+str(query['QueryNumber'])+'.csv', 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                writer.writerow(query['Column Names'])
                for row in query['Query Result']:
                    writer.writerow(row)

    # Write output into a database
    def writeDB(self, data):
        try:
            conn = DBManager.DBManager.getConnection('../OutputFiles/ResultDB/OutputQueries')

            DBManager.DBManager.InitResultDB(conn)

            for query in data:
                insertBuilder = InsertBuilder.InsertBuilder(query['QueryNumber'])

                #DBManager.DBManager.deleteAllRows(conn, insertBuilder.getTableName())
                DBManager.DBManager.insertRows(conn, insertBuilder.getInsertStatement(), query['Query Result'])

                conn.commit()
        except Exception as e:
            print('Error writing to DB')
            print(e)
        finally:
            DBManager.DBManager.closeConnection(conn)
