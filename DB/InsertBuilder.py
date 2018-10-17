from DB import DBManager


class InsertBuilder:

    queryValuesTemplates = ('(?,?,?,?,?)',  # 1
                            '(?,?,?,?,?)',  # 2
                            '(?,?)',        # 3
                            '(?,?)',        # 4
                            '(?,?,?)',      # 4
                            '(?,?)',        # 6
                            '(?)')          # 7

    def __init__(self, queryNum):
        self.insertStatement = 'INSERT INTO Query' + str(queryNum+1) +\
                              ' VALUES ' + InsertBuilder.queryValuesTemplates[queryNum]
        self.tableName = 'Query' + str(queryNum+1)

    def getInsertStatement(self):
        return self.insertStatement
    def getTableName(self):
        return self.tableName

