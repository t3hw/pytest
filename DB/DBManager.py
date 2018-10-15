import sqlite3
from sqlite3 import Error
from metadata import Singleton


class DBManager(Singleton):
    conn = None

    def getConnection(self, db_file):
        try:
            if self.conn is None:
                self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()

    def select(self, statement):
        cur = self.conn.cursor()
        cur.execute(statement)

        rows = cur.fetchall()
        return rows

    def insert(self, statement, args):
        cur = self.conn.cursor()
        cur.execute(statement, args)
        return cur.lastrowid
