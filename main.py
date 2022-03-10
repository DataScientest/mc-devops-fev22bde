from fastapi import FastAPI
import requests
import os

api = FastAPI()


@api.get('/')
def get_index():
    return {
        "status": 1
    }


@api.get('/temperature')
def get_temperature(lat: float, lon: float):
    response = requests.get(
        url="https://api.openweathermap.org/data/2.5/weather",
        params={
            "lat": lat,
            "lon": lon,
            "appid": os.environ.get("API_KEY")
        }
    )

    data = response.json()
    return {
        "lat": lat,
        "lon": lon,
        "temp": data["main"]["temp"]
    }
