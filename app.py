import json

from flask import Flask, request, jsonify
from flask_cors import CORS

import autoaiApi
import database
import report
from config import *

app = Flask(__name__)
CORS(app)


@app.route('/predict/<claim_number>', methods=['GET', 'POST'])
def get_predicted_value(claim_number):
    conn = database.openDB(dbFile=database_name)
    row = database.fetchRecord(conn, table_name, claim_number)

    params = jsonify(row)
    print(params)
    is_fraud, fraud_percentage = autoaiApi.predict(params)
    return str(fraud_percentage)


@app.route('/report', methods=['GET', 'POST'])
def get_report():
    return report.getAllData()


@app.route('/getrecord/<claim_number>', methods=['GET'])
def get_record(claim_number):
    conn = database.openDB(dbFile=database_name)
    row = database.fetchRecord(conn, table_name, claim_number)
    params = jsonify(row).data
    is_fraud, fraud_percentage = autoaiApi.predict(params)
    return str(fraud_percentage)


@app.route('/updaterecord/<claim_number>', methods=['GET', 'POST'])
def update_record(claim_number):
    conn = database.openDB(dbFile=database_name)
    database.updateRecord(conn,
                          table_name,
                          claim_number,
                          request.form.keys)
    row = database.fetchRecord(conn, table_name, claim_number)
    params = jsonify(row).data
    is_fraud, fraud_percentage = autoaiApi.predict(params)
    return str(fraud_percentage)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
