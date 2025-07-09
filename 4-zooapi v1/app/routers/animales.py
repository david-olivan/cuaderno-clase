from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError
from ..models.animales import Animal
from ..models.respuestas import RespuestaNormal, RespuestaError, Error

router = APIRouter(prefix="/animales", tags=["Los Animales"])

animales_db = [
    {"nombre": "cabra"},
    {"nombre": "búho"},
    {
        "nombre": "pulpo",
        "edad": 5,
        "familia": "cefalópodos",
        "vivo": True
    }
]

@router.get("")
async def leer_animales() -> RespuestaNormal:
    datos_validados = []

    for item in animales_db:
        try: 
            datos_validados.append(Animal(**item))
        except ValidationError:
            pass

    return RespuestaNormal(
        data=datos_validados,
        message= "Tus animales, entregados por tu router de confianza"
    )

@router.get("/{animal_id}")
async def leer_animal(animal_id: int) -> RespuestaNormal:
    if len(animales_db) < animal_id + 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return RespuestaNormal(
        data=animales_db[animal_id],
        message="Animal encontrado, aquí lo tienes"
    )
    
    
@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_animal(animal: Animal) -> RespuestaNormal:
    animales_db.append(animal.model_dump())
    
    return RespuestaNormal(
        data= animal,
        message= "Animal creado correctamente"
    )


# Aquí documento el 404 que tiramos nosotros directamente, a través de modelos de pydantic
@router.put("/{animal_id}", responses={404: {"model": RespuestaError} })
async def modificar_animal(animal_id: int, animal: Animal) -> RespuestaNormal:
    if len(animales_db) < animal_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=Error(message="Ha ido mal").model_dump())

    mod_animal = animal

    animales_db[animal_id] = mod_animal.model_dump()

    return RespuestaNormal(
        data=mod_animal,
        message="Animal modificado"
    )

@router.delete("/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def borrar_animal(animal_id: int):
    if len(animales_db) > animal_id:
        animales_db.remove(animales_db[animal_id])
