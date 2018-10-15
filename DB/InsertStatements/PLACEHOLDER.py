from DB import DBManager


class PLACEHOLDER:
    SQL = ''' INSERT INTO placeholder(one,two,three)
              VALUES(?,?,?) '''

    @staticmethod
    def insert(one, two, three):
        row = (one, two, three)
        DBManager.DBManager().insert(PLACEHOLDER.SQL, row)

