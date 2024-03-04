from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/countries/{country_name}")
async def country(country_name: str = "japan", city_name: str = "tokyo"):
    return {
        "country_name": country_name,
        "city_name": city_name
    }

#http://127.0.0.1:8000/countries/america?city_name=new_york

@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }

