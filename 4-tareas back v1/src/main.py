import time
from faker import Faker
from fastapi import FastAPI, status, HTTPException

from tareas.DocumentController import get_tasks, set_tasks
from tareas.schemas import Tarea, TareaUpdate

app = FastAPI(
    title="DavsTasks",
    version="0.0.1",
    description="Un ejemplo de API para clase.",
    root_path="/api/v1"
)


@app.get("/")
async def index():
    return {"tareas": "http://127.0.0.1:8000/tareas"}


@app.get(
        "/tareas",
        description="Muestra todas las tareas de un usuario",
        tags=["Tareas"]
)
async def get_tareas():
    tareas = get_tasks("fran")
    return tareas


@app.get("/tareas/{task_id}", tags=["Tareas"])
async def get_tareas_by_id(task_id: str):
    return search_by_id("fran", task_id)


@app.post("/tareas", tags=["Tareas"], status_code=status.HTTP_201_CREATED)
async def create_tarea(tarea: Tarea):
    fk = Faker()
    tarea.id = (
        str(time.time()).replace(".", "")
        + fk.random_letter()
        + fk.random_letter()
        + fk.random_letter()
    )
    tareas = get_tasks("fran")
    tareas.append(tarea.model_dump())
    set_tasks("fran", tareas)
    return {"message": "Tarea creada adecuadamente", "id": tarea.id}


@app.put("/tareas/{task_id}", tags=["Tareas"], status_code=status.HTTP_202_ACCEPTED)
async def modify_tarea_by_id(task_id: str, modificacion: TareaUpdate):
    tarea_a_modificar = search_by_id("fran", task_id)
    if len(tarea_a_modificar) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La tarea con id {task_id} no existe")
    
    tarea_a_modificar = tarea_a_modificar[0]
    nuevos_datos = modificacion.model_dump(exclude_unset=True)

    listado_tareas = get_tasks("fran")
    indice_tarea = listado_tareas.index(tarea_a_modificar)

    tarea_a_modificar.update(nuevos_datos)
    listado_tareas[indice_tarea] = tarea_a_modificar

    set_tasks("fran", listado_tareas)
    return tarea_a_modificar



@app.delete("/tareas/{task_id}", tags=["Tareas"])
async def delete_tarea_by_id(task_id: str):
    tarea_a_borrar = search_by_id("fran", task_id)
    if len(tarea_a_borrar) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La tarea con id {task_id} no existe")
    
    listado_tareas = get_tasks("fran")
    listado_tareas.remove(tarea_a_borrar[0])
    set_tasks("fran", listado_tareas)
    return {"message": "Tarea borrada adecuadamente"}


def search_by_id(username: str, id: str):
    """
    Encuentra una tarea para un determinado usuario con un id concreto

    Args:
        username (str): El usuario cuyas tareas queremos examinar
        id (str): El id que queremos buscar

    Returns:
        list: El listado de tareas cuyo id coincide con la búsqueda
    """
    listado_tareas = get_tasks(username)
    # for tarea in listado_tareas:
    #     if tarea.id == id:
    #         return [tarea]
    return [tarea for tarea in listado_tareas if tarea["id"] == id]
