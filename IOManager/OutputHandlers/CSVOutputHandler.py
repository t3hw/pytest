from IOManager import IO
import os
import csv


class CSVOutputHandler(IO.IO):

    def write(self, data):
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
