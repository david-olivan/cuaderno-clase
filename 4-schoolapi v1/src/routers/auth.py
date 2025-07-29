from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
import secrets

from ..database import API_Keys 


class APIRequest(BaseModel):
    role: str


class APIResponse(APIRequest):
    api_key: str


roles = ["admin", "user", "test"]


router = APIRouter(prefix="/auth", tags=["API Keys"])

@router.post("/new", status_code=status.HTTP_201_CREATED, response_model=APIResponse)
async def create_new_key(request: APIRequest):
    if request.role not in roles:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="El rol seleccionado no está disponible")

    # Generar nueva api_key, hashearla y guardarla
    raw_key = await generate_new_key(request.role)

    # Devolver la api_key plana al usuario
    return APIResponse(role=request.role, api_key=raw_key)


@router.get("/me")
async def read_role(api_key: str):
    # Validar la api_key y devolver el role del usuario
    role = validate_api_key()

    return { "message": f"Tu rol es {role}."}


# TODO implementar
async def generate_new_key(role: str) -> str:
    raw_key = "S-API-" + secrets.token_urlsafe(32)

    # Hashearé todo, y lo guardaré en la base de datos
    # TODO hashear y almacenar el hash con salt
    await API_Keys(api_key=raw_key, role=role).create()

    return raw_key


# TODO implementar
async def validate_api_key(): ...