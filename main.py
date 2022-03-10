from fastapi import FastAPI

api = FastAPI()


@api.get('/')
def get_index():
    return {
        "status": 1
    }


@api.get('/temperature')
def get_temperature(lat: float, lon: float):
    return {
        "lat": lat,
        "lon": lon
    }
