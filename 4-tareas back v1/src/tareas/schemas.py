from pydantic import BaseModel


class Tarea(BaseModel):
    id: str
    name: str
    priority: int
    description: str | None = None
    project: str
    assigned_to: list[str] | None = None
    completed: bool = False


class TareaUpdate(BaseModel):
    name: str | None = None
    priority: int | None = None
    description: str | None = None
    project: str | None = None
    assigned_to: list[str] | None = None
    completed: bool | None = None
