from tareas.DocumentController import get_tasks, set_tasks
from tareas.schemas import Tarea


def main():
    ...


def add_task(username: str, nueva_tarea: Tarea):
    # cargar todas las tareas
    tareas_actuales = get_tasks(username)
    # hacer un append a la lista
    tareas_actuales.append(nueva_tarea.model_dump())
    # guardar la lista
    set_tasks(username, tareas_actuales)


if __name__ == "__main__":
    main()
