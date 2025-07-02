from pydantic import BaseModel


class Tarea(BaseModel):
    id: str
    name: str
    priority: int
    description: str | None = None
    project: str
    assigned_to: list[str] | None = None
