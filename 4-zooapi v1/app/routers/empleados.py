from fastapi import APIRouter

router = APIRouter(prefix="/empleados", tags=["Los Empleados"])

empleados_db =[{"nombre": "Jaime"}, {"nombre": "Dani"}]

@router.get("/")
async def leer_empleados():
    return {
        "success": True,
        "data": empleados_db,
        "message": "Todos los empleados"
    }