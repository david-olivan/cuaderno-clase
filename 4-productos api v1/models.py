from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List


class GenericResponse(BaseModel):
    success: bool = True
    data: List
    message: str


class categoria(str, Enum):
    ELECTRONICA = "electrónica"
    ORDENADORES = "ordenadores"
    MOVILES = "móviles"


class ProductoRequest(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    precio: float = Field(ge=5.0)
    description: Optional[str] = None
    category: categoria


class ProductoResponse(BaseModel):
    id: int
    name: str
    precio: float
    description: Optional[str]
    category: categoria
