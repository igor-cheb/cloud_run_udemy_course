from fastapi import FastAPI
from .env import CONFIG

MODE = CONFIG("mode", default="test")

app = FastAPI()

@app.get("/")
def home_page():
    return {"Hello": "Hello, you!", "mode": MODE}