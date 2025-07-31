import asyncio
from faker import Faker
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


class API_Keys(Document):
    api_key: str
    role: str

    class Settings:
        name = "apikeys"


MONGO_URL = str(config("MONGO_URL"))


async def init_db():
    client = AsyncIOMotorClient(MONGO_URL)
    database = client["schoolapi"]
    await init_beanie(database=database, document_models=[Estudiante, Curso, API_Keys])  # type: ignore


async def seed_everything():
    await init_db()

    fk = Faker()

    student_input = int(input("Cuantos estudiantes quieres: "))
    curso_input = int(input("Cuantos cursos quieres: "))

    for _ in range(student_input):
        await Estudiante(
            name=fk.name(),
            edad=fk.random_int(min=18, max=120),
            ciudad=fk.city()
        ).create()

    modalidades_posibles = ["presencial", "híbrido", "aula virtual", "online"]
    for _ in range(curso_input):
        await Curso(
            name=fk.sentence(3),
            duration=fk.random_int(min=25, max=520),
            modalidad=modalidades_posibles[fk.random_int(min=0, max=3)]
        ).create()


if __name__ == "__main__":
    asyncio.run(seed_everything())    

    