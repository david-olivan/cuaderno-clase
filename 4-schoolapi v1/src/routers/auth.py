from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import secrets
import bcrypt
from typing import Optional

from ..database import API_Keys 

# Establecemos el tipo de seguridad para nuestra autenticación, en este caso
# Bearer, que deberá ser cómo se envíe la API key dentro del header Authentication
security = HTTPBearer()

# Modelo de pydantic para validar las peticiones de creación de api keys
class APIRequest(BaseModel):
    role: str

# Modelo de pydantic para definir cómo se envían las api keys recién creadas
# Extiende el modelo de APIRequest
class APIResponse(APIRequest):
    api_key: str

# Posibles roles que se pueden asignar a una api key al ser creada
roles = ["admin", "user", "test"]

# Router para poder 'exportar' todas las rutas de auth al archivo principal
router = APIRouter(prefix="/auth", tags=["API Keys"])


async def generate_new_key(role: str) -> str:
    """
    Esta función genera nuevas API keys y les asigna el rol solicitado.

    Parameters:
        role (str): The role that will be assigned to the api key

    Returns:
        str: The plain text api key that the user will have to keep
    """
    # Utilizo secrets y un prefijo para crear una api key segura en texto plano
    raw_key = "S-API-" + secrets.token_urlsafe(32)

    # Genero salt usando el algoritmo de bcrypt directamente
    salt = bcrypt.gensalt()
    # Hasheo la api key de texto plano pasándola a bytes on .encode() y añadiendo salt
    hashed_key = bcrypt.hashpw(raw_key.encode(), salt)
    # Guardo la versión hasheada junto con el rol asignado en la base de datos
    await API_Keys(api_key=hashed_key.decode(), role=role).create()

    # Devuelvo la clave en texto plano
    return raw_key


async def validate_api_key(raw_key: str) -> Optional[str]:
    """
    Valida una api key contra los hashes que están almacenados en my base de datos.

    Parameters:
        raw_key(str): La api key en texto plano que será validada

    Returns:
        str: El rol asignado a esa api key, si es válida

    Raises:
        HTTPException: Si la api key no es válida
    """
    # Saco todas las api keys de la base de datos y las paso a lista
    keys = await API_Keys.find_all().to_list()

    # Hago un bucle y comparo la api key en texto plano contra mi listado de hashes
    for item in keys:
        # Comparo con bcrypt pasando ambos elementos a bytes primero
        if bcrypt.checkpw(raw_key.encode(), item.api_key.encode()):
            # Si hay coincidencia, devuelvo el rol correspondiente
            return item.role
    # Si llego hasta aquí quiere decir que no hay una api key válida así que tiro error
    raise HTTPException(401, detail="Pasame una API Key válida")


async def get_api_key_from_headers(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Optional[str]:
    """
    Extrae las credenciales del header Authorization, tipo Bearer

    Parameters:
        credentials(HTTPAuthorizationCredentials): El valor (scheme y datos) del header Authorization

    Returns:
        str: El rol asociado a esa api key

    Raises:
        HTTPException: Si no hay api key o falta un header Authorization: Bearer
    """
    # Si no hay credenciales
    if credentials is None:
        # Tiro un error
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Es necesaria una API Key para usar este endpoint")
    
    # Si encuentro credenciales se las paso a la función de validarlas
    role = await validate_api_key(credentials.credentials)

    # Si llego hasta aquí quiere decir que esta api key tiene un role así que lo devuelvo
    return role


@router.post("/new", status_code=status.HTTP_201_CREATED, response_model=APIResponse)
async def create_new_key(request: APIRequest):
    """
    Recibe una petición para generar una nueva api key.

    Parameters:
        request(APIRequest): Un objeto que contiene un posible rol para una nueva api key.

    Returns:
        APIResponse: El rol junto con la api key en texto plano.

    Raises:
        HTTPException: Si el rol solicitado no está en la lista de roles válidos.
    """
    # Si el rol solicitado no está en la lista
    if request.role not in roles:
        # Tiro un error
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="El rol seleccionado no está disponible")

    # Llamo a la función para generar nuevas api keys que he definido más arriba
    raw_key = await generate_new_key(request.role)

    # Devolver la api_key plana al usuario
    return APIResponse(role=request.role, api_key=raw_key)


@router.get("/me")
async def read_role(role: str = Depends(get_api_key_from_headers)):
    """
    Esta ruta de POST devuelve el rol asignado a la api key que requiere. Utiliza dependencias
    de FastAPI para requerir dicha api key.

    Parameters:
        role(str): El resultado de la dependencia de llamar a la función de conseguir los headers de seguridad.
    Returns:
        Dict[str, str]: El mensaje en el que se confirma el rol.
    """
    return { "message": f"Tu rol es {role}."}

