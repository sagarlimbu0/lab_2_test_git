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


# testing for bad input parameters
# def teest_hello_bad_parameter():
#     response= client.get("/hello?sam=name")

#     assert response.status_code ==422
#     assert response.json() == {
#         "detail":[
#         {
#             "loc":["query", "name"],
#             "msg": "field required",
#             "type": "value_error.missing",
#         }
#         ]
#     }

@pytest.mark.parametrize(
    "input_name, expected",
    [("sam", "sam"), ("Nessan", "Nessan"), (100, 100)],
)

def test_name(input_name, expected):
    response= client.get(f"/hello?name={input_name}")
    
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {expected}"}


def test_docs():

    response= client.get("/docs")
    assert response.status_code == 200
    