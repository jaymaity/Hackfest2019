import json

from watson_machine_learning_client import WatsonMachineLearningAPIClient

from config import *

WML_CREDENTIALS = {
    "url": key_url,
    "apikey": api_key,
    "instance_id": instance_id
}

SCHEMA = {
    "CLAIM_NUMBER",
    "INCIDENT_TYPE",
    "ACTIONTAKEN",
    "LOSS_TYPE",
    "STATE",
    "LIABILITY",
    "SEGMENT",
    "INVESTIGATED",
    "LOSS_DATE",
    "POLICY_EFFECTIVE",
    "POLICY_EXPIRATION",
    "INSURED_NAME",
    "INSURED_AGE",
    "DEBT",
    "potential_fraudster",
    "Fraud_complete",
    "fraud_potential",
    "fraud_risk_level",
    "fraud_used",
    "hit_and_run_ind",
    "icbc_keymissingstolen",
    "icbc_keyswithvehicle",
    "icbc_numvehiclekeyset",
    "totalloss",
    "vehlockind",
    "vehstolenind",
    "veh_towed_ind",
    "case_status",
    "policy_inception_days",
    "days_rem_policy_expiry",
    "loss_date_month",
    "loss_date_year",
    "policy_expiration_month",
    "policy_expiration_year",
    "policy_effective_month",
    "policy_effective_year",
    "NOTES"
}

NULL_LIST = {"CLAIM_NUMBER",
             "STATE",
             "LOSS_DATE",
             "POLICY_EFFECTIVE",
             "POLICY_EXPIRATION",
             "Fraud_complete",
             "hit_and_run_ind",
             "vehstolenind",
             "veh_towed_ind",
             "NOTES",
             "policy_effective_month"
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

    is_fraud = predictions["predictions"][0]["values"][0][0] == 1.0
    fraud_percentage = predictions["predictions"][0]["values"][0][1][1]

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
            if key in NULL_LIST:
                values.append(None)
            else:
                values.append(params[key])

    # Taking care of key that are not present
    non_populated_keys = set(schema) - set(keys)
    for key in non_populated_keys:
        keys.append(key)
        values.append(None)
    return keys, values
