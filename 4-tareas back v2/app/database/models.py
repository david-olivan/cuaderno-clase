from sqlmodel import SQLModel, Field
from typing import Optional, List


class Proyecto(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    name: str
    description: Optional[str]
    tareas: str
    lead: str


class Tarea(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    name: str
    prioridad: int
    asignado_a: str
    completed: bool = False