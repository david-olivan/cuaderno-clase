from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status, Depends
from .database import init_db, Estudiante, Curso
from beanie import PydanticObjectId
from pydantic import BaseModel
from typing import Optional

from .routers import estudiantes, auth


class CursoRequest(BaseModel):
    name: str
    duration: int
    modalidad: Optional[str] = None


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


@app.get("/cursos", tags=["Cursos"])
async def get_cursos():
    cursos = await Curso.find_all().to_list()
    return cursos

endpoint_auth = {403: {}, 401: {}}

@app.post("/cursos", tags=["Cursos"], status_code=201, responses=endpoint_auth) # type: ignore
async def crear_curso(curso: CursoRequest, role: str = Depends(auth.get_api_key_from_headers)):
    if role == "admin":
        nuevo_curso = await Curso(**curso.model_dump()).create()
        return {"message": "Curso creado correctamente", "data": nuevo_curso}
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Tu rol actual no permite la creación de cursos")

app.include_router(estudiantes.router)