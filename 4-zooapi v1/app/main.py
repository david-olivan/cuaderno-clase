from fastapi import FastAPI
from .routers import animales, inventario, empleados
from .models.respuestas import RespuestaNormal


app = FastAPI(
    title="ZooAPI",
    version="0.0.1",
)

endpoints = ["/animales", "/inventario", "/empleados"]

@app.get("/", tags=["index"])
async def index():
    return RespuestaNormal(
        data=endpoints,
        message="Bienvenido a ZooAPI 0.0.1, aquí tienes los recursos disponibles"
    )


app.include_router(animales.router)
app.include_router(inventario.router)
app.include_router(empleados.router)