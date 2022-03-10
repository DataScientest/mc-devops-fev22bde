from fastapi import FastAPI

api = FastAPI()


@api.get('/')
def get_index():
    return {
        "status": 1
    }