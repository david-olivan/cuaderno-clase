from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status, Depends
from .database import init_db, Curso
from pydantic import BaseModel
from typing import Optional

from .routers import estudiantes, auth, cursos


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="School API",
    version="0.0.1",
    description="Otro ejemplo de API más",
)


@app.get("/", tags=["Health Check"])
async def health_check():
    return {"message": "Todo OK"}


app.include_router(auth.router)
app.include_router(estudiantes.router)
app.include_router(cursos.router)