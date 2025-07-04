import time
from faker import Faker
from fastapi import FastAPI, status, HTTPException

from tareas.DocumentController import get_tasks, set_tasks
from tareas.schemas import Tarea, TareaUpdate

app = FastAPI(
    title="DavsTasks",
    version="0.0.1",
    description="Un ejemplo de API para clase.",
    root_path="/api/v1",
)  # Las propiedades con las que instancio FastAPI me permiten describir mi API, poner la versión y nombre así como la url base


@app.get("/")
async def index():
    """
    Me devuelve los endpoints de la API

    Returns:
        dict: Los endpoints de la API
    """
    return {"tareas": "http://127.0.0.1:8000/tareas"}


@app.get(
    "/tareas", description="Muestra todas las tareas de un usuario", tags=["Tareas"]
)
async def get_tareas():
    """
    Saca todas las tareas del almacenamiento y las devuelve en base a un usuario

    Returns:
        list[dict]: La lista de tareas, cada una de ellas con un diccionario
    """
    tareas = get_tasks("fran")  # Cargo la lista de tareas desde el almacenamiento
    return tareas  # La devuelvo


@app.get("/tareas/{task_id}", tags=["Tareas"])
async def get_tareas_by_id(task_id: str):
    """
    Devuelve una tarea según id si está en el almacenamiento

    Args:
        task_id (str): El id de la tarea que se quiere buscar

    Returns:
        list[dict]: Un listado con la tarea que corresponde o vacío si no se ha encontrado
    """
    return search_by_id("fran", task_id)  # Llamo a la función de búsqueda por id


@app.post("/tareas", tags=["Tareas"], status_code=status.HTTP_201_CREATED)
async def create_tarea(tarea: Tarea):
    """
    Crea una nueva tarea de los datos del body y la guarda en el almacenamiento

    Args:
        tarea (Tarea): Una tarea según el esquema de Pydantic que hemos definido. Validación automática.

    Returns:
        dict: Mensaje de éxito y el id de la nueva tarea
    """
    fk = Faker()  # Creo una instancia de Faker
    tarea.id = (
        str(time.time()).replace(".", "")
        + fk.random_letter()
        + fk.random_letter()
        + fk.random_letter()
    )  # Uso la instacia de Faker para sobreescribir el id que me haya llegado con uno propio
    tareas = get_tasks("fran")  # Cargo la lista desde almacenamiento
    tareas.append(
        tarea.model_dump()
    )  # Añado la tarea a la lista, convirtiéndola de Tarea que es un modelo de Pydantic a dict de python con model_dump()
    set_tasks("fran", tareas)  # Guardo la nueva lista de tareas
    return {
        "message": "Tarea creada adecuadamente",
        "id": tarea.id,
    }  # Devuelvo mensaje de éxito con el id de la tarea


@app.put(
    "/tareas/{task_id}", tags=["Tareas"], status_code=status.HTTP_202_ACCEPTED
)  # Si la operación tiene éxito, devolveremos un código 202 porque lo he configurado aquí
async def modify_tarea_by_id(task_id: str, modificacion: TareaUpdate):
    """
    Modifico una tarea según el id que se ponga en la url

    Args:
        task_id (str): El id de la tarea que quiero modificar
        modificacion (TareaUpdate): Recibe del body de la petición (porque es un modelo de Pydantic) las propiedades que se pueden modificar, en este caso como Tarea pero opcionales todos

    Returns:
        dict: La tarea modificada
    """
    tarea_a_modificar = search_by_id("fran", task_id)  # Busco la tarea por id
    if (
        len(tarea_a_modificar) == 0
    ):  # Si la lista no tiene nada, su longitud será 0, la tarea no ha sido encontrada
        # Así que tiraré un error usando fastapi, de código 404 como que no la he encontrado
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La tarea con id {task_id} no existe",
        )

    tarea_a_modificar = tarea_a_modificar[
        0
    ]  # Si sí que tengo tarea, tengo que reasignar la variable para no tener que indexar la lista todo el rato
    nuevos_datos = modificacion.model_dump(
        exclude_unset=True
    )  # Hago un dump de los nuevos valores a modificar, usando model_dump con la opción exclude_onset para recibir solamente las propiedades con valor

    listado_tareas = get_tasks("fran")  # Cargo todas las tareas desde el almacenamiento
    indice_tarea = listado_tareas.index(
        tarea_a_modificar
    )  # Me guardo el índice de la tarea original

    tarea_a_modificar.update(
        nuevos_datos
    )  # Modifico los valores de la tarea original con el método de diccionario .update y el dump de propiedades que he hecho antes
    listado_tareas[indice_tarea] = (
        tarea_a_modificar  # Indexo la lista y sustituyo la tarea original de la lista por la nueva tarea modificada
    )

    set_tasks("fran", listado_tareas)  # Guardo la lista modifica
    return tarea_a_modificar  # Y devuelvo la tarea con los nuevos valores (buenas prácticas para un PUT)


@app.delete("/tareas/{task_id}", tags=["Tareas"])
async def delete_tarea_by_id(task_id: str):
    """
    Borra una tarea según id

    Args:
        task_id (str): El id de la tarea a borrar

    Returns:
        dict: Mensaje de éxito
    """
    tarea_a_borrar = search_by_id(
        "fran", task_id
    )  # Busco la tarea por id, recibo una lista vacía o con 1 tarea
    if (
        len(tarea_a_borrar) == 0
    ):  # Si la longitud es 0, no hay tarea a borrar, el id no existe
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La tarea con id {task_id} no existe",
        )

    listado_tareas = get_tasks("fran")  # Cargo las tareas desde almacenamiento
    listado_tareas.remove(
        tarea_a_borrar[0]
    )  # Borro la lista usando el valor de la tarea con la función .remove de las listas de python. Tengo que indexar porque tarea_a_borrar es una lista
    set_tasks("fran", listado_tareas)  # Guardo la lista de tareas modificada
    return {"message": "Tarea borrada adecuadamente"}  # Devuelvo el mensaje de éxito


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
