from IOManager import IO
from DB import InsertBuilder, DBManager


class DBOutputHandler(IO.IO):

    def write(self, data):
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
