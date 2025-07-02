import json

def get_tasks(username: str) -> list:
    """
    Devuelve la lista de tareas para un usuario determinado

    Si el JSON de ese usuario no existe, crea el archivo con una tarea vacía

    Args:
        username (str): El usuario cuyas tareas queremos leer
    Returns:
        list: La lista de tareas, o un mensaje en lista de que se ha creado el archivo JSON
    """
    try:
        with open(f"documents/{username}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(f"documents/{username}.json", "w", encoding="utf-8") as file:
            json.dump([], file)
            return ["Archivo creado con []"]


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