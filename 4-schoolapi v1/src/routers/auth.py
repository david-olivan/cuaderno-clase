from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import secrets
import bcrypt
from typing import Optional

from ..database import API_Keys 


security = HTTPBearer()

class APIRequest(BaseModel):
    role: str


class APIResponse(APIRequest):
    api_key: str


roles = ["admin", "user", "test"]


router = APIRouter(prefix="/auth", tags=["API Keys"])




async def generate_new_key(role: str) -> str:
    raw_key = "S-API-" + secrets.token_urlsafe(32)

    # Hashearé todo, y lo guardaré en la base de datos
    salt = bcrypt.gensalt()
    hashed_key = bcrypt.hashpw(raw_key.encode(), salt)
    await API_Keys(api_key=hashed_key.decode(), role=role).create()

    return raw_key


async def validate_api_key(raw_key: str) -> Optional[str]:
    keys = await API_Keys.find_all().to_list()

    for item in keys:
        # Comparar api keys
        if bcrypt.checkpw(raw_key.encode(), item.api_key.encode()):
            return item.role
        
    raise HTTPException(401, detail="Pasame una API Key válida")


async def get_api_key_from_headers(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Optional[str]:
    if credentials is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Es necesaria una API Key para usar este endpoint")
    
    role = await validate_api_key(credentials.credentials)

    return role


@router.post("/new", status_code=status.HTTP_201_CREATED, response_model=APIResponse)
async def create_new_key(request: APIRequest):
    if request.role not in roles:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="El rol seleccionado no está disponible")

    # Generar nueva api_key, hashearla y guardarla
    raw_key = await generate_new_key(request.role)

    # Devolver la api_key plana al usuario
    return APIResponse(role=request.role, api_key=raw_key)


@router.get("/me")
async def read_role(role: str = Depends(get_api_key_from_headers)):
    return { "message": f"Tu rol es {role}."}

