from pydantic import BaseModel

class Empleado(BaseModel):
    nombre: str
    edad: int
    puesto: str
    activo: bool
