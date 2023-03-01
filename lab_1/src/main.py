from fastapi import FastAPI, Query, Path, Form
import openapi

app= FastAPI()

@app.get("/hello")
async def get_name( name: str ):
    if name:
        return {"hello":name}
    else:
        return {"Client Error Response, (400 - 499)": "Please Enter a Name"}

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

