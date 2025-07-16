from sqlmodel import create_engine, Session


DB_URL = "sqlite:///app/database/sqlite.db"

engine = create_engine(DB_URL, echo=True)

async def get_session():
    with Session(engine) as session:
        yield session