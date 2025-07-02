from DocumentController import set_tasks
from schemas import Tarea
from faker import Faker
import time


def seed_tareas(cantidad: int, username: str):
    fk = Faker()

    listado = []
    for _ in range(cantidad):
        tarea = Tarea(
            id=str(time.time()).replace(".", "") + fk.random_letter() + fk.random_letter() + fk.random_letter(),
            name=fk.sentence(6),
            priority=fk.random_int(1, 3),
            project=fk.sentence(3),
            assigned_to=[fk.name() for _ in range(fk.random_int(1, 5))]
            )
        listado.append(tarea.model_dump())

    set_tasks(username, listado)


if __name__ == "__main__":
    cantidad = int(input("Cantidad: "))
    username = input("Username: ")
    seed_tareas(cantidad, username)
