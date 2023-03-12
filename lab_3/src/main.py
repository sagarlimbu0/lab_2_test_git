# from fastapi import FastAPI, Query, Request, Response
# #from fastapi.encoders import jsonable_encoder
# import openapi
# from pydantic import BaseModel, ValidationError, validator, Field
# import joblib
# #from flask import Flask, jsonify, request
# import numpy as np
# from sklearn.pipeline import Pipeline
# from datetime import datetime



# app= FastAPI()

# # pydantic model
# # input data
# class housingInput(BaseModel):
    
#     MedInc: float = Field(ge= 1)
#     HouseAge: float
#     AveRooms: float
#     AveBedrms: float
#     Population: float
#     AveOccup: float
#     Latitude: float
#     Longitude: float

#     # Raise Error if room numbers more than 6
#     @validator("Latitude")
#     def check_rooms(cls, v):
#         if float(v) > 90:
#             raise ValueError('invalid coordinates')
#         return v

#     # @validator("MedInc", "HouseAge", "AveRooms")
#     # def check_data_type(cls, v)

# # output data
# class predictOutput(BaseModel):
#     MedHouseVal: float

# @app.get("/hello")
# async def get_name( name: str ):
#     return {"message": f"Hello {name}"}

# @app.get("/")
# async def not_implemented():
#     return {"not implemented"}

# ## Load ml model
# svr_model = joblib.load("model_pipeline.pkl")

# features= joblib.load("features.pkl")
# # pipeline for data transformation

# @app.post("/predict")
# async def predict(request: Request):
   
#     json_list= await request.json()
    
#     # passing the first list item (JSON object)
#     # parsing through Pydantic model
#     input= housingInput.parse_obj(json_list)

#     test_data=[[
#         input.MedInc, 
#         input.HouseAge,
#         input.AveRooms,
#         input.AveBedrms,
#         input.Population,
#         input.AveOccup,
#         input.Latitude,
#         input.Longitude
#     ]]
    
#     # verify if model is available
#     if not svr_model:
#         raise RuntimeError("Model not loaded")

#    # check for extra inputs
#     row, load_features= np.array(test_data).shape
    
#     if len(features) != load_features:
#         raise ValueError("Extra Input of Features Loaded")

#     prediction= svr_model.predict(test_data)[0]
 
#     return predictOutput(MedHouseVal= prediction)

# # Health Check
# @app.get("/health")
# async def get_datetime():

#     return {"DateTime": datetime.now().isoformat()}

   





import numpy as np
from fastapi import FastAPI, HTTPException
from joblib import load
from pydantic import BaseModel, Extra

app = FastAPI()
model = load("model_pipeline.pkl")


# Use pydantic.Extra.forbid to only except exact field set from client.
# This was not required by the lab.
# Your test should handle the equivalent whenever extra fields are sent.
# class House(BaseModel, extra=Extra.forbid):
class House(BaseModel, extra=Extra.forbid):
    """Data model to parse the request body JSON."""

    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

    def to_np(self):
        return np.array(list(vars(self).values())).reshape(1, 8)


class HousePrediction(BaseModel):
    prediction: float


@app.post("/predict", response_model=HousePrediction)
async def predict(house: House):
    prediction = model.predict(house.to_np())
    return {"prediction": prediction}


@app.get("/health")
async def health():
    return {"status": "healthy"}


# Raises 422 if bad parameter automatically by FastAPI
@app.get("/hello")
async def hello(name: str):
    return {"message": f"Hello {name}"}




