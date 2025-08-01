from pydantic import BaseModel
from typing import Optional

class CursoOptional(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class CursoRequest(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
