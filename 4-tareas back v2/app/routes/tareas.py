from fastapi import APIRouter, status, Depends
from sqlmodel import Session, select
from pydantic import BaseModel
from ..controllers.tareas import get_tareas
from ..database.database import get_session
from ..database.models import Tarea as TareaDB

class TareaRequest(BaseModel):
    name: str
    prioridad: int
    asignado_a: str


router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

@router.get("")
async def leer_tareas(session: Session = Depends(get_session)):
    operacion = select(TareaDB)
    tareas = session.exec(operacion).all()
    return tareas

@router.get("/{tarea_id}")
async def leer_tarea(tarea_id: int, session: Session = Depends(get_session)):
    tarea = session.get_one(TareaDB, tarea_id)
    return tarea if tarea else {"message": "No hay tarea con este id"}

@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_tarea(tarea: TareaRequest, session: Session = Depends(get_session)):
    nueva_tarea: TareaDB = TareaDB(**tarea.model_dump())
    # Cargar operación de guardado en la sesión
    session.add(nueva_tarea)
    # Guardar operaciones
    session.commit()
    return {"message": "Tarea guardada"}

@router.put("/{tarea_id}")
async def actualizar_tarea(tarea_id: int):
    return {"message": "Ha funcionado"}

@router.delete("/{tarea_id}")
async def borrar_tarea(tarea_id: int):
    return {"message": "Ha funcionado"}