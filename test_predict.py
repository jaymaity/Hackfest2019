from unittest import TestCase
from autoaiApi import *


class TestPredict(TestCase):
    def test_json_values(self):
        keys , values = parse_json_values("""{ "name":"John", "age":30, "car":null }""")
        assert keys == ["name", "age", "car"]
        assert values == ["John", 30, None]

    def test_predict(self):
        json_string = """{ "CLAIM_NUMBER":null, 
          "INCIDENT_TYPE":"VehicleIncident", 
          "LOSS_TYPE":"Vandalism", 
          "STATE": "Open",
          "LIABILITY": "Deny", 
          "SEGMENT": null,
          "INVESTIGATED": "No",
          "LOSS_DATE": null, 
          "POLICY_EFFECTIVE": null,
          "POLICY_EXPIRATION": null,
          "INSURED_NAME": null,
          "INSURED_AGE": 26,
          "DEBT":350 }"""
        value = predict(json_string)
        print(value)

