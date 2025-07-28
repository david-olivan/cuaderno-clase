from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie
from typing import Optional
from decouple import config


class Estudiante(Document):
    name: str
    edad: int
    ciudad: Optional[str] = None

    class Settings:
        name = "estudiantes"


class Curso(Document):
    name: str
    duration: int
    modalidad: Optional[str] = None

    class Settings:
        name = "cursos"


MONGO_URL = str(config("MONGO_URL"))


async def init_db():
    client = AsyncIOMotorClient(MONGO_URL)
    database = client["schoolapi"]
    await init_beanie(database=database, document_models=[Estudiante, Curso])  # type: ignore
