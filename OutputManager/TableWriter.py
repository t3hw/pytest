from OutputManager import FileWriter
from DB import InsertBuilder, DBManager


class TableWriter(FileWriter.FileWriter):
    def write(self, data):
        try:
            conn = DBManager.DBManager.getConnection('../OutputFiles/ResultDB/OutputQueries')

            for i, query in enumerate(data):
                insertBuilder = InsertBuilder.InsertBuilder(i)

                DBManager.DBManager.deleteAllRows(conn, insertBuilder.getTableName())
                DBManager.DBManager.insertRows(conn, insertBuilder.getInsertStatement(), query['Query Result'])

                conn.commit()
        except Exception as e:
            print(e)
        finally:
            DBManager.DBManager.closeConnection(conn)
