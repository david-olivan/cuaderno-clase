from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from pydantic import BaseModel

# Todas estas variables
SECRET_KEY = "27f240bb65e8760fa3365dd0b970ed3b5626e6629c5366deb5c3b27ef479"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

FAKE_DB = {}

# Modelos
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

app = FastAPI()


# Funciones auxiliares
def get_user(db: dict, username: str) -> UserInDB | None: 
    if username in db:
        user = db[username]
        return UserInDB(**user)
    

def authenticate_user(db: dict, username: str, password: str): 
    user = get_user(db, username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_time: timedelta | None = None): 
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_time or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]): 
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Tú no tienes token, así que no pasas",
        headers={"WWW-Authenticate": "Bearer"}
    )

    # Inteot decodificar el token para sacar el usuario
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_error
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise credentials_error
    
    # Validar que el usuario está en la base de datos
    user = get_user(FAKE_DB, username=token_data.username or "")
    if user is None:
        raise credentials_error
    # Devolver usuario
    return user


@app.get("/")
async def index():
    return "Hola"

@app.get("/me")
async def read_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

class NewUser(BaseModel):
    username: str
    password: str

@app.post("/user")
async def create_user(user: NewUser):
    new_user = UserInDB(
        username=user.username,
        hashed_password=pwd_context.hash(user.password)
    )
    FAKE_DB[new_user.username] = new_user.model_dump()

    return FAKE_DB


@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(
        FAKE_DB,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    expire_time = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_time=expire_time
    )

    return Token(access_token=access_token, token_type="bearer")
