from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError
from ..models.empleados import Empleado
from ..models.respuestas import RespuestaNormal, RespuestaError, Error

router = APIRouter(prefix="/empleados", tags=["Los Empleados"])

empleados_db = [
    {
        "nombre": "Juan",
        "edad": 30,
        "puesto": " cuidador",
        "activo": True
    },
    {
        "nombre": "Ana",
        "edad": 25,
        "puesto": "veterinaria",
        "activo": True
    }
]

@router.get("")
async def leer_empleados() -> RespuestaNormal:
    datos_validados = []

    for item in empleados_db:
        try: 
            datos_validados.append(Empleado(**item))
        except ValidationError:
            pass

    return RespuestaNormal(
        data=datos_validados,
        message= "Tus empleados, entregados por tu router de confianza"
    )

@router.get("/{empleado_id}")
async def leer_empleado(empleado_id: int) -> RespuestaNormal:
    if len(empleados_db) < empleado_id + 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return RespuestaNormal(
        data=empleados_db[empleado_id],
        message="Empleado encontrado, aquí lo tienes"
    )
    
    
@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_empleado(empleado: Empleado) -> RespuestaNormal:
    empleados_db.append(empleado.model_dump())
    
    return RespuestaNormal(
        data= empleado,
        message= "Empleado creado correctamente"
    )


# Aquí documento el 404 que tiramos nosotros directamente, a través de modelos de pydantic
@router.put("/{empleado_id}", responses={404: {"model": RespuestaError} })
async def modificar_empleado(empleado_id: int, empleado: Empleado) -> RespuestaNormal:
    if len(empleados_db) < empleado_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=Error(message="Ha ido mal").model_dump())

    mod_empleado = empleado

    empleados_db[empleado_id] = mod_empleado.model_dump()

    return RespuestaNormal(
        data=mod_empleado,
        message="Empleado modificado"
    )

@router.delete("/{empleado_id}", status_code=status.HTTP_204_NO_CONTENT)
async def borrar_empleado(empleado_id: int):
    if len(empleados_db) > empleado_id:
        empleados_db.remove(empleados_db[empleado_id])
