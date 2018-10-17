from OutputManager import FileWriter
import csv


class CSVFileWriter(FileWriter.FileWriter):
    def write(self, data):

        for i,query in enumerate(data):
            with open('./OutputFiles/CSV/Query'+str(i+1)+'.csv', 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, dialect='excel')
                writer.writerow(query['Column Names'])
                for row in query['Query Result']:
                    writer.writerow(row)
