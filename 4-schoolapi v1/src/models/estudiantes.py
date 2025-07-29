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