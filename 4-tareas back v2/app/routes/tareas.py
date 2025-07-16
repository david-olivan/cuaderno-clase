from fastapi import APIRouter
from pydantic import BaseModel
from ..controllers.tareas import get_tareas

class TareaRequest(BaseModel): ...

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

@router.get("")
async def leer_tareas():
    return await get_tareas()

@router.get("/{tarea_id}")
async def leer_tarea(tarea_id: int):
    return {"message": "Ha funcionado"}

@router.post("")
async def crear_tarea(tarea: TareaRequest):
    return {"message": "Ha funcionado"}

@router.put("/{tarea_id}")
async def actualizar_tarea(tarea_id: int):
    return {"message": "Ha funcionado"}

@router.delete("/{tarea_id}")
async def borrar_tarea(tarea_id: int):
    return {"message": "Ha funcionado"}