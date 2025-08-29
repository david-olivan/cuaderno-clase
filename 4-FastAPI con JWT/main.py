from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from pydantic import BaseModel

# Todas estas variables deberíamos tenerlas en el entorno o en .env
SECRET_KEY = "27f240bb65e8760fa3365dd0b970ed3b5626e6629c5366deb5c3b27ef479"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Creamos un contexto para hashear las contraseñas y verificarlas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Creamos un scheme de autenticación para poder utilizar una dependencia más adelante
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Base de datos falsa en memoria, será un diccionario username-usuario
FAKE_DB = {}

# Modelos de pydantic para validación
# Cuando enviemos un token de vuelta lo haremos con este modelo
class Token(BaseModel):
    access_token: str
    token_type: str

# Cuando extraigamos los datos de un usuario del token lo haremos con este modelo
class TokenData(BaseModel):
    username: str | None = None

# La base de usuarios, solamente con el nombre
class User(BaseModel):
    username: str

# Los usuarios en Base de datos tendrán, además, la contraseña hasheada
class UserInDB(User):
    hashed_password: str


# Instanciamos FastAPI
app = FastAPI()


# Funciones auxiliares
# Con esta función extraemos el usuario de la base de datos si existe, si no, devolvemos None
def get_user(db: dict, username: str) -> UserInDB | None: 
    if username in db:
        user = db[username]
        return UserInDB(**user)
    
# Con esta función autenticamos un usuario
def authenticate_user(db: dict, username: str, password: str): 
    # Llamamos a la función auxiliar anterior
    user = get_user(db, username)
    # Si esta no nos devuelve un usuario o la contraseña de este usuario no corresponde con su hash, devolvemos False
    if not user or not pwd_context.verify(password, user.hashed_password):
        return False
    # Si llegamos hasta aquí, todo correcto, así que devuelve el usuario entero
    return user

# Creamos un token usando los datos de input para el payload
def create_access_token(data: dict, expires_time: timedelta | None = None): 
    # Copia profunda de los datos de entrada para poder manipularlos en una nueva variable
    to_encode = data.copy()
    # Calculamos el moment en el que expirará sumando el tiempo de duración a la fecha y hora actual
    expire = datetime.now(timezone.utc) + (expires_time or timedelta(minutes=15))
    # Actualizamos el payload añadiendo este nuevo claim al diccionario
    to_encode.update({"exp": expire})
    # Devolvemos la versión codificada del token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Esta función depende del scheme de oauth2 y a su vez se usará como dependencia en cada endpoint
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]): 
    # Establecemos un tipo de excepción para todos los errores de credenciales
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Tú no tienes token, así que no pasas",
        headers={"WWW-Authenticate": "Bearer"}
    )

    # Intento decodificar el token para sacar el usuario
    try:
        # Saco el payload usando jwt para decodificarlo
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Busco el usuario asignado a este token dentro del payload
        username = payload.get("sub")
        # Si no encuentro nada en este claim, tiro error
        if username is None:
            raise credentials_error
        # Si sí que hay algo, lo valido a través de un tokendata que he definido
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        # Si el token no es válido, saldrá este error y lo corresponderé con la excepción que he definido anteriormente
        raise credentials_error
    
    # Validar que el usuario está en la base de datos con la función definida previamente
    user = get_user(FAKE_DB, username=token_data.username or "")
    # Si me devuelve none, tiro error
    if user is None:
        raise credentials_error
    # Devolver usuario si llego hasta aquí porque es válido y todo bien
    return user


@app.get("/")
async def index():
    return "Hola"

# Este es un endpoint protegido el cual requerirá un usuario actual
@app.get("/me")
async def read_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

# Con esta clase puedo requerir usuario y contraseña para crear usuarios
# Manera de testear este flujo sin una base de datos permanente
class NewUser(BaseModel):
    username: str
    password: str

# Con este endpoint crearé nuevos usuarios para testear
@app.post("/user")
async def create_user(user: NewUser):
    # Genero un nuevo usuario del tipo que almacenaré en la "base de datos"
    new_user = UserInDB(
        username=user.username,
        hashed_password=pwd_context.hash(user.password) # Hasheando la contraseña
    )
    # Indexaré el diccionario usando el nombre de usuario y haré un dump del modelo entero
    FAKE_DB[new_user.username] = new_user.model_dump()

    # Devuelvo la "base de datos" entera para comprobar que ha funcionado
    return FAKE_DB

# Con este endpoint, que tiene una dependencia de un Request Form, genero nuevos tokens para usuarios válidos
@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    # Autentico el usuario con la función auxiliar anterior
    user = authenticate_user(
        FAKE_DB,
        form_data.username,
        form_data.password
    )

    # Si no hay usuario, tiro excepción
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Si llego hasta aquí el usuario todo guay, así que calculo tiempo de expiración del token
    expire_time = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Y genero el token asegurándome de guardar en "sub" el usuario y añadir el tiempo de expirar
    access_token = create_access_token(
        data={"sub": user.username},
        expires_time=expire_time
    )
    
    # Devuelvo el token usando el modelo de datos previamente definido
    return Token(access_token=access_token, token_type="bearer")
