from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from sqlmodel import Session, select
from .database import get_session, Animal

class AnimalRequest(BaseModel):
    name: str = Field(description="El nombre del animal", min_length=3, max_length=50)
    edad: int = Field(description="La edad del animal", gt=0)
    bioma: Optional[str] = None

app = FastAPI(
    title="ZooAPI",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_headers="*",
    allow_methods="*"
)


@app.get("/")
async def index():
    return {
        "success": True,
        "data": {
            "endpoints": [
                "/animales"
            ]
        }
    }

@app.get("/animales", tags=["Animales"])
async def leer_animales(session: Session = Depends(get_session)):
    operacion = select(Animal)
    animales = session.exec(operacion).all()
    return animales

@app.get("/animales/{animal_id}", tags=["Animales"])
async def leer_animal(animal_id: int, session: Session = Depends(get_session)):
    animal = session.get_one(Animal, animal_id)
    return animal

@app.post("/animales", tags=["Animales"])
async def add_animal(animal: AnimalRequest, session: Session = Depends(get_session)):
    nuevo_animal = Animal(**animal.model_dump())
    session.add(nuevo_animal)
    session.commit()
    session.refresh(nuevo_animal)
    return nuevo_animal

@app.put("/animales/{animal_id}", tags=["Animales"])
async def modificar_animal(animal_id: int):
    return {"Todo guay"}

@app.delete("/animales/{animal_id}", tags=["Animales"])
async def borrar_animal(animal_id: int):
    return {"Todo guay"}
