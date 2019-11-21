from flask import Flask, request, jsonify
import autoaiApi
import report
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods = ['GET', 'POST'])
def get_predicted_value():
    params = jsonify(request.form).data
    print(params)
    is_fraud, fraud_percentage =  autoaiApi.predict(params)
    return str(fraud_percentage)


@app.route('/report', methods = ['GET', 'POST'])
def get_report_l():
    print("aaa")
    return report.getAllData()


if __name__ == '__main__':
    app.run(host='0.0.0.0')