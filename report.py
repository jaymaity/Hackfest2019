import sqlite3
from config import *
import json


def getAllData():
    conn = sqlite3.connect(database=database_name)
    c = conn.cursor()
    rows = c.execute("select CLAIM_NUMBER, LOSS_DATE, INSURED_NAME, pred_fraud_percent from ClaimsFraudPrepT WHERE "
                     "pred_fraud_percent IS NOT NULL").fetchall()

    tuple_rows = list(map(lambda a: (a[0], a[1], a[2],), rows))
    # for r in rows:
    #     print(r)
    jsondump = json.dumps(tuple_rows)
    #print(jsondump)
    conn.commit()
    conn.close()
    return jsondump