from pydantic import BaseModel

class Jaula(BaseModel):
    tipo: str
    fuerza: int


class Animal(BaseModel):
    nombre: str
    edad: int
    familia: str
    vivo: bool
    jaula: Jaula | None = None
