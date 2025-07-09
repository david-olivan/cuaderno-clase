from fastapi import APIRouter

router = APIRouter(prefix="/inventario", tags=["El Inventario"])

inventario_db = [{"nombre": "comida para cabras"}, {"nombre": "comida para pulpos"}, {"nombre": "comida para búhos"}]

@router.get("/")
async def leer_inventario():
    return {
        "success": True,
        "data": inventario_db,
        "message": "Tu inventario completo"
    }