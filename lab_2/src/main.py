from fastapi import FastAPI, Query, Request, Response
#from fastapi.encoders import jsonable_encoder
import openapi
from pydantic import BaseModel, ValidationError, validator, Field
import joblib
#from flask import Flask, jsonify, request
import numpy as np
from sklearn.pipeline import Pipeline
from datetime import datetime



app= FastAPI()

# pydantic model
# input data
class housingInput(BaseModel):
    
    MedInc: float = Field(ge= 1)
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

    # Raise Error if room numbers more than 6
    @validator("Latitude")
    def check_rooms(cls, v):
        if float(v) > 90:
            raise ValueError('invalid coordinates')
        return v

    # @validator("MedInc", "HouseAge", "AveRooms")
    # def check_data_type(cls, v)

# output data
class predictOutput(BaseModel):
    MedHouseVal: float

@app.get("/hello")
async def get_name( name: str ):
    return {"message": f"Hello {name}"}

@app.get("/")
async def not_implemented():
    return {"not implemented"}

@app.get("/docs")
async def get_docs():
    url= f'https://swagger.io/specification/'
    return {"url": str(url)}

@app.get("/openapi.json")
async def get_version():
    return {"version": openapi.__version__}

## Load ml model
svr_model = joblib.load("model_pipeline.pkl")

features= joblib.load("features.pkl")
# pipeline for data transformation
#def pipeline_(arr):


@app.post("/predict")
async def predict(request: Request):
   
    json_list= await request.json()
    
    # passing the first list item (JSON object)
    # parsing through Pydantic model
    input= housingInput.parse_obj(json_list[0])

    test_data=[[
        input.MedInc, 
        input.HouseAge,
        input.AveRooms,
        input.AveBedrms,
        input.Population,
        input.AveOccup,
        input.Latitude,
        input.Longitude
    ]]
    
    # verify if model is available
    if not svr_model:
        raise RuntimeError("Model not loaded")

   # check for extra inputs
    row, load_features= np.array(test_data).shape
    
    if len(features) != load_features:
        raise ValueError("Extra Input of Features Loaded")

    prediction= svr_model.predict(test_data)[0]
 
    return predictOutput(MedHouseVal= prediction)

# Health Check
@app.get("/health")
async def get_datetime():

    return {"DateTime": datetime.now().isoformat()}

   