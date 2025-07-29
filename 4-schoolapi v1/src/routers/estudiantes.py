from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId

from ..database import Estudiante
from ..models.estudiantes import EstudianteOptional, EstudianteRequest

router = APIRouter()

@router.get("/estudiantes", tags=["Estudiantes"])
async def get_estudiantes():
    estudiantes = await Estudiante.find_all().to_list()
    return estudiantes


@router.get(
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


@router.post("/estudiantes", tags=["Estudiantes"], status_code=201)
async def crear_estudiante(student: EstudianteRequest):
    nuevo_estudiante = await Estudiante(**student.model_dump()).create()
    return {"message": "Estudiante creado correctamente", "data": nuevo_estudiante}


@router.put("/estudiantes/{student_id}", tags=["Estudiantes"])
async def modificar_estudiante(
    student_id: PydanticObjectId, student: EstudianteOptional
):
    estudiante = await db_get_estudiante(student_id)
    await estudiante.set(student.model_dump(exclude_unset=True))
    return {"message": f"Estudiante con id {student_id} ha sido modificado"}


@router.delete("/estudiantes/{student_id}", tags=["Estudiantes"])
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
