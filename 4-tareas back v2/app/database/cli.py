from sys import argv
import os
from database import engine
from sqlmodel import SQLModel
from models import Proyecto, Tarea


if __name__ == "__main__":
    if len(argv) > 1:
        match(argv[1]):
            case "db:recreate":
                os.remove("app/database/sqlite.db")
                SQLModel.metadata.create_all(engine)
            case "db:create":
                SQLModel.metadata.create_all(engine)
            case "db:delete":
                os.remove("app/database/sqlite.db")