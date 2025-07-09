from pydantic import BaseModel

class RespuestaNormal(BaseModel):
    success: bool = True
    data: object
    message: str

class Error(BaseModel):
    success: bool = False
    message: str

class RespuestaError(BaseModel):
    detail: Error