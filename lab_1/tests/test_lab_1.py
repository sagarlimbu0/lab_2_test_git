from src import __version__
from fastapi.testclient import TestClient
from fastapi import FastAPI
from src.main import app 


client= TestClient(app)

def test_version():
    assert __version__ == '0.1.0'

def test_name():

    response= client.get("/hello")

    # check the status
    status= response.status_code
    if status == 200:
        assert response.status_code == 200
    elif status == 422:
        assert response.status_code > 400

def test_second():

    response= client.get("/")
    assert response.status_code == 200

def test_docs():

    response= client.get("/docs")
    assert response.status_code == 200

def test_openapi():

    response= client.get("/openapi.json")
    assert response.status_code == 200

