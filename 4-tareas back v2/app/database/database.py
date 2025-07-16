from sqlmodel import create_engine


DB_URL = "sqlite:///app/database/sqlite.db"

engine = create_engine(DB_URL, echo=True)

