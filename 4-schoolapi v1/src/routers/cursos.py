from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId

from ..database import Curso
from ..models.cursos import CursoOptional, CursoRequest

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.get("/")
async def get_cursos():
    cursos = await Curso.find_all().to_list()
    return cursos

@router.get(
    "/{curso_id}",
    responses={
        404: {
            "description": "No hay ningún curso con ese id",
            "content": {
                "application/json": {
                    "example": {"detail": "No hay ningún curso con ese id"}
                }
            },
        }
    },
)
async def get_curso(curso_id: PydanticObjectId):
    curso = await db_get_curso(curso_id)
    return curso

@router.post("/", status_code=201)
async def crear_curso(curso: CursoRequest):
    nuevo_curso = await Curso(**curso.model_dump()).create()
    return {"message": "Curso creado correctamente", "data": nuevo_curso}

@router.put("/{curso_id}")
async def modificar_curso(
    curso_id: PydanticObjectId, curso: CursoOptional
):
    curso_db = await db_get_curso(curso_id)
    await curso_db.set(curso.model_dump(exclude_unset=True))
    return {"message": f"Curso con id {curso_id} ha sido modificado"}

@router.delete("/{curso_id}")
async def borrar_curso(curso_id: PydanticObjectId):
    curso = await db_get_curso(curso_id)
    await curso.delete()
    return {"message": "Curso borrado correctamente"}

async def db_get_curso(curso_id: PydanticObjectId) -> Curso:
    """
    Recibe un id de curso, lo busca en la base de datos y si no lo encuentra
    tira una excepción tipo HTTPException con código de error 404

    @returns curso - Curso
    """
    curso = await Curso.get(curso_id)
    if not curso:
        raise HTTPException(404, detail="No existe un curso con este id")
    return curso