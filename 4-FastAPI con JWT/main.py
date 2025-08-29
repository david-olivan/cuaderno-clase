from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from pydantic import BaseModel

# Variables, constantes y setup
SECRET_KEY = "27f240bb65e8760fa3365dd0b970ed3b5626e6629c5366deb5c3b27ef479"
ALGORITHM = "HS256"
TOKEN_EXPIRE_TIME = 15

FAKE_DB = {}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Modelos
class Token(BaseModel):
    token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

# Funciones auxiliares

# Creación de FastAPI
app = FastAPI()

# Endpoints
@app.get("/")
async def index(): ...

@app.get("/me")
async def read_user(): ...

@app.post("/new-user")
async def create_user(): ...