from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

class AnimalRequest(BaseModel):
    name: str = Field(description="El nombre del animal", min_length=3, max_length=50)
    edad: int = Field(description="La edad del animal", gt=0)
    mote: Optional[str]

app = FastAPI(
    title="ZooAPI",
    version="2.0.0"
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

@app.get("/animales")
async def leer_animales():
    return {"Todo guay"}

@app.get("/animales/{animal_id}")
async def leer_animal(animal_id: int):
    return {"Todo guay"}

@app.post("/animales")
async def add_animal(animal: AnimalRequest):
    return {"Todo guay"}

@app.put("/animales/{animal_id}")
async def modificar_animal(animal_id: int):
    return {"Todo guay"}

@app.delete("/animales/{animal_id}")
async def borrar_animal(animal_id: int):
    return {"Todo guay"}
