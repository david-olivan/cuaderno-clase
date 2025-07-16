from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import tareas, usuarios, proyectos

app = FastAPI(
    title="Tareas API",
    version="2.0.0",
    description="Segunda versión de nuestra querida API de tareas",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_headers="*",
    allow_methods="*"
)

app.include_router(tareas.router)
app.include_router(usuarios.router)
app.include_router(proyectos.router)


@app.get("/")
async def index():
    return {"message": "Estos son los endpoints", "endpoints": ["/tareas", "/usuarios", "/proyectos"]}

