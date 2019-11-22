import sqlite3
# Connect .db
def openDB(dbFile):
    return sqlite3.connect(dbFile)


# retrieve one record of the claim number from a table
def fetchRecord(conn, tableName ,ClaimNumber):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    number=(ClaimNumber,)
    c.execute('SELECT * '
              'FROM '+ tableName + ' '
              'WHERE CLAIM_NUMBER=?',
              number)

    return dict(c.fetchone())

# update all records of the claim number from a table
def updateRecord(conn,tableName, ClaimNumber, Params):
    c = conn.cursor()

    tableInfo =c.execute('pragma table_info('+tableName+')').fetchall()
    colsUpdated =''
    for i in tableInfo:
        colsUpdated += i[1] + ','

    newValues = Params + (ClaimNumber,)

    c.execute('UPDATE ' + tableName + ' SET ' +
              colsUpdated.rstrip(',') +
              'where claim_number =?', newValues)
    conn.commit()

# Sample Code
# dbFileName = 'C:\\BigDataTools_Projects\\Hackfest2019\\fraud_detection.db'
# db = openDB(dbFileName)
# tableName = 'test'
# print(fetchRecord(db,tableName,'FFFFCFABBBC665B14234100C4B25451D'))
# updateRecord(db,tableName,'FFFF9910C8FD3CE4E38469785552F7AE',fetchRecord(db,tableName,'FFFFCFABBBC665B14234100C4B25451D'))


