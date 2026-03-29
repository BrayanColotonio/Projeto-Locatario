from fastapi import FastAPI
from app.routes.vehicle_routes import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "API rodando"}
