import json
import time
from faker import Faker
from tareas.schemas import Tarea


def get_tasks(username: str) -> list:
    """
    Devuelve la lista de tareas para un usuario determinado

    Si el JSON de ese usuario no existe, crea el archivo con una tarea vacía

    Args:
        username (str): El usuario cuyas tareas queremos leer
    Returns:
        list: La lista de tareas, o un mensaje en lista de que se ha creado el archivo JSON
    """
    fk = Faker()
    try:
        with open(f"documents/{username}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(f"documents/{username}.json", "w", encoding="utf-8") as file:
            tarea = Tarea(
                id=str(time.time()).replace(".", "")
                + fk.random_letter()
                + fk.random_letter()
                + fk.random_letter(),
                name=fk.sentence(6),
                priority=fk.random_int(1, 3),
                project=fk.sentence(3),
                assigned_to=[fk.name() for _ in range(fk.random_int(1, 5))],
            )
            json.dump(tarea.model_dump(), file)
            return [tarea.model_dump()]


def set_tasks(username: str, listado_tareas: list[dict]):
    """
    Guarda la lista de tareas para un usuario determinado

    Args:
        username (str): El usuario cuyas tareas queremos guardar
        listado_tareas (list[dict]): La lista de tareas que queremos guardar

    Returns:
        str: Mensaje de confirmación de que las tareas han sido escritas
    """
    with open(f"documents/{username}.json", "w", encoding="utf-8") as file:
        json.dump(listado_tareas, file)
    return "Archivo escrito correctamente"
