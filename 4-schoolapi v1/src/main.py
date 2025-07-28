from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from .database import init_db, Estudiante, Curso
from beanie import PydanticObjectId
from pydantic import BaseModel
from typing import Optional


class EstudianteOptional(BaseModel):
    name: Optional[str] = None
    edad: Optional[int] = None
    ciudad: Optional[str] = None


class EstudianteRequest(BaseModel):
    name: str
    edad: int
    ciudad: Optional[str] = None


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


@app.get("/cursos", tags=["Cursos"])
async def get_cursos():
    cursos = await Curso.find_all().to_list()
    return cursos


@app.post("/cursos", tags=["Cursos"], status_code=201)
async def crear_curso(curso: CursoRequest):
    nuevo_curso = await Curso(**curso.model_dump()).create()
    return {"message": "Curso creado correctamente", "data": nuevo_curso}


@app.get("/estudiantes", tags=["Estudiantes"])
async def get_estudiantes():
    estudiantes = await Estudiante.find_all().to_list()
    return estudiantes


@app.get(
    "/estudiantes/{student_id}",
    tags=["Estudiantes"],
    responses={
        404: {
            "description": "No hay ningún estudiante con ese id",
            "content": {
                "application/json": {
                    "example": {"detail": "No hay ningún estudiante con ese id"}
                }
            },
        }
    },
)
async def get_estudiante(student_id: PydanticObjectId):
    estudiante = await db_get_estudiante(student_id)
    return estudiante


@app.post("/estudiantes", tags=["Estudiantes"], status_code=201)
async def crear_estudiante(student: EstudianteRequest):
    nuevo_estudiante = await Estudiante(**student.model_dump()).create()
    return {"message": "Estudiante creado correctamente", "data": nuevo_estudiante}


@app.put("/estudiantes/{student_id}", tags=["Estudiantes"])
async def modificar_estudiante(
    student_id: PydanticObjectId, student: EstudianteOptional
):
    estudiante = await db_get_estudiante(student_id)
    await estudiante.set(student.model_dump(exclude_unset=True))
    return {"message": f"Estudiante con id {student_id} ha sido modificado"}


@app.delete("/estudiantes/{student_id}", tags=["Estudiantes"])
async def borrar_estudiante(student_id: PydanticObjectId):
    estudiante = await db_get_estudiante(student_id)
    await estudiante.delete()
    return {"message": "Estudiante borrado correctamente"}


async def db_get_estudiante(student_id: PydanticObjectId) -> Estudiante:
    """
    Recibe un id de estudiante, lo busca en la base de datos y si no lo encuentra
    tira una excepción tipo HTTPException con código de error 404

    @returns estudiante - Estudiante
    """
    estudiante = await Estudiante.get(student_id)
    if not estudiante:
        raise HTTPException(404, detail="No existe un estudiante con este id")
    return estudiante
