from pydantic import BaseModel

class Categoria(BaseModel):
    nombre: str
    descripcion: str

class InventarioItem(BaseModel):
    nombre: str
    cantidad: int
    descripcion: str
    categoria: Categoria
