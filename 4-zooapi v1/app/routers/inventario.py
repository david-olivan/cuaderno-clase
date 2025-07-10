from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError
from ..models.inventario import InventarioItem, Categoria
from ..models.respuestas import RespuestaNormal, RespuestaError, Error

router = APIRouter(prefix="/inventario", tags=["El Inventario"])

inventario_db = [
    {
        "nombre": "comida para cabras",
        "cantidad": 100,
        "descripcion": "Comida especial para cabras montesas",
        "categoria": {
            "nombre": "Alimentos",
            "descripcion": "Comida y suplementos para los animales"
        }
    },
    {
        "nombre": "comida para pulpos",
        "cantidad": 50,
        "descripcion": "Comida para pulpos de anillos azules",
        "categoria": {
            "nombre": "Alimentos",
            "descripcion": "Comida y suplementos para los animales"
        }
    },
    {
        "nombre": "comida para búhos",
        "cantidad": 75,
        "descripcion": "Comida para búhos nivals",
        "categoria": {
            "nombre": "Alimentos",
            "descripcion": "Comida y suplementos para los animales"
        }
    }
]

@router.get("")
async def leer_inventario() -> RespuestaNormal:
    datos_validados = []

    for item in inventario_db:
        try:
            datos_validados.append(InventarioItem(**item))
        except ValidationError:
            pass

    return RespuestaNormal(
        data=datos_validados,
        message="Tu inventario completo"
    )

@router.get("/{item_id}")
async def leer_item(item_id: int) -> RespuestaNormal:
    if len(inventario_db) < item_id + 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return RespuestaNormal(
        data=inventario_db[item_id],
        message="Item encontrado, aquí lo tienes"
    )
    
    
@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_item(item: InventarioItem) -> RespuestaNormal:
    inventario_db.append(item.model_dump())
    
    return RespuestaNormal(
        data=item,
        message="Item creado correctamente"
    )


@router.put("/{item_id}", responses={404: {"model": RespuestaError}})
async def modificar_item(item_id: int, item: InventarioItem) -> RespuestaNormal:
    if len(inventario_db) < item_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=Error(message="Ha ido mal").model_dump())

    mod_item = item

    inventario_db[item_id] = mod_item.model_dump()

    return RespuestaNormal(
        data=mod_item,
        message="Item modificado"
    )

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def borrar_item(item_id: int):
    if len(inventario_db) > item_id:
        inventario_db.remove(inventario_db[item_id])
