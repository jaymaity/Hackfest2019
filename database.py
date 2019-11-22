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
    row = c.fetchone()
    if row:
        return dict(row)
    else:
        return None

# update all records of the claim number from a table
def updateRecord(conn,tableName, ClaimNumber, KeyValues):
    c = conn.cursor()

    # tableInfo =c.execute('pragma table_info('+tableName+')').fetchall()
    colsUpdated =''
    # for i in tableInfo:
    #     colsUpdated += i[1] + ','
    for i in KeyValues.keys():
        colsUpdated += i + '=?,'

    newValues = tuple(KeyValues.values()) + (ClaimNumber,)

    c.execute('UPDATE ' + tableName + ' SET ' +
              colsUpdated.rstrip(',') +
              'where claim_number =?', newValues)
    conn.commit()

# Sample Code
# dbFileName = 'C:\\BigDataTools_Projects\\Hackfest2019\\fraud_detection.db'
# db = openDB(dbFileName)
# tableName = 'claimsfraudprept'
# updateRecord(db,tableName,'B7EF1BDD73571FF675637211882C8BC1',fetchRecord(db,tableName,'B7EF1BDD73571FF675637211882C8BC1'))


