import sqlite3
from config import *
import json


def getAllData():
    conn = sqlite3.connect(database=database_name)
    c = conn.cursor()
    rows = c.execute("select CLAIM_NUMBER, INSURED_NAME, pred_fraud_percent from {table_name} WHERE "
                     "pred_fraud_percent IS NOT NULL ORDER BY pred_fraud_percent DESC".format(
        table_name=table_name)).fetchall()

    tuple_rows = list(map(lambda a: "{\"CLAIM_NUMBER\":\"" + str(a[0]) + "\",\"INSURED_NAME\":\"" + str(a[1])+"\","
                                                                                                       "\"pred_fraud_percent\":\"" + str(a[2])+"\"}",
                          rows))
    json_str = "[" + ",".join(tuple_rows)  + "]"

    jsondump = json.dumps(tuple_rows)
    #print(jsondump)
    conn.commit()
    conn.close()
    return json_str