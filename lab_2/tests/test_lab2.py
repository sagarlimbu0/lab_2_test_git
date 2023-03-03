from src import __version__
from fastapi.testclient import TestClient
from fastapi import FastAPI
from src.main import app 
import pytest
import json
from datetime import datetime

client= TestClient(app)

def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize(
    "input_name, expected",
    [("sam", "sam"), ("nessan", "nessan")]
)

def test_name(input_name, expected):
    response= client.get(f"/hello?name={input_name}")
    
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {expected}"}

def test_second():

    response= client.get("/")
    assert response.status_code == 200

def test_docs():

    response= client.get("/docs")
    assert response.status_code == 200

def test_openapi():

    response= client.get("/openapi.json")
    assert response.status_code == 200


# TEST inputs
# @pytest.mark.parametrize(
#     "input_features",
#     #, status_code",
#     [
#         [{
#             "MedInc": 22.0, 
#             "HouseAge": 33.4, 
#             "AveRooms": 2, 
#             "AveBedrms": 5.8, 
#             "Population": 322.0, 
#             "AveOccup": 3, 
#             "Latitude": 35,
#             "Longitude": -122.25
#     }],
#     #, 200]
# ])

# Test Correct Input Features
# def test_correct_input(input_features):
#     response= client.put("/predict",
#         content= json.dumps(input_features))

#     data_= json.loads(response.json())

#     assert 'data' in data_
#     assert 'MedInc' in data_['MedInc']
#     assert 'HouseAge' in data_['HouseAge']
#     assert 'AveRooms' in data_['AveRooms']
#     assert 'AveBedrms' in data_['AveBedrms']
#     assert 'Population' in data_['Population']
#     assert 'AveOccup' in data_['AveOccup']
#     assert 'Latitude' in data_['Latitude']
#     assert 'Longitude' in data_['Longitude']

## TEST INPUT on json format
# @pytest.mark.parametrize(
#     "input_features",
#     #, status_code",
#     [
#         [{
#             "MedInc": 22.0, 
#             "HouseAge": 33.4, 
#             "AveRooms": 2, 
#             "AveBedrms": 5.8, 
#             "Population": 322.0, 
#             "AveOccup": 3, 
#             "Latitude": 35,
#             "Longitude": -122.25
#     }],
#     #, 200]
# ])

# input_features_= {
#             "MedInc": 22.0, 
#             "HouseAge": 33.4, 
#             "AveRooms": 2, 
#             "AveBedrms": 5.8, 
#             "Population": 322.0, 
#             "AveOccup": 3, 
#             "Latitude": 35,
#             "Longitude": -122.25
#     }

# def test_input_features(input_features_):

#     response= client.put("/predict",
#         content= json.dumps(input_features_))

#     assert response.json() == input_features_
#    # assert response.status_code == status_code


## test health endpoint
def test_health():
    response= client.get("/health")
    curr_dateTime= response.json()

    assert datetime.fromisoformat(curr_dateTime["DateTime"])





