import json

from watson_machine_learning_client import WatsonMachineLearningAPIClient

from config import *

WML_CREDENTIALS = {
    "url": key_url,
    "apikey": api_key,
    "instance_id": instance_id
}

SCHEMA = {
    'INCIDENT_TYPE', 'Y', 'LOSS_TYPE', 'STATE', 'LIABILITY',
    'SEGMENT', 'INVESTIGATED', 'INSURED_AGE', 'DEBT', 'INSURED_NAME',
    'policy_inception_days', 'days_rem_policy_expiry', 'loss_date_month', 'loss_date_year',
    'policy_expiration_month', 'policy_expiration_year', 'policy_effective_month', 'policy_effective_year'
}


def predict(parameters):
    """
    Predicts percentage of fraud
    :param parameters:
    :return:
    """
    # Parse json
    fields, values = parse_json_values(parameters, schema=SCHEMA)

    # Creates connection and gets the predicted value
    client = WatsonMachineLearningAPIClient(WML_CREDENTIALS)
    scoring_payload = {"input_data": [{"fields": fields, "values": [values]}]}
    predictions = client.deployments.score(deployment_url, scoring_payload)

    is_fraud = predictions["predictions"][0]["values"][0][0]
    fraud_percentage = predictions["predictions"][0]["values"][0][1][2]

    return is_fraud, fraud_percentage


def parse_json_values(json_string, schema):
    """
    Parse json string values and produces list of keys and values
    Expected input format: { "name":"John", "age":30, "car":null }
    :param json_string:
    :return:
    """
    params = json.loads(json_string)
    keys = []
    values = []
    for key in params:
        if key in schema:
            keys.append(key)
            values.append(params[key])

    # Taking care of key that are not present
    non_populated_keys = schema - set(keys)
    for key in non_populated_keys:
        keys.append(key)
        values.append(None)
    return keys, values
