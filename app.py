from flask import Flask, request, jsonify
import autoaiApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods = ['GET', 'POST'])
def get_predicted_value():
    params = jsonify(request.form).data
    print(params)
    is_fraud, fraud_percentage =  autoaiApi.predict(params)
    return str(fraud_percentage)


if __name__ == '__main__':
    app.run()