from fastapi import FastAPI, HTTPException
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
    try:
        response = requests.get(
            url="https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": lat,
                "lon": lon,
                "appid": os.environ.get("API_KEY")
            }
        )

        data = response.json()
        temp = data["main"]["temp"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
        "lat": lat,
        "lon": lon,
        "temp": temp
    }
