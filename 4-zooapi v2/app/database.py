from sqlmodel import SQLModel, create_engine, Field, Session, select
from typing import Optional

class Bioma(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Animal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    edad: int
    bioma: Optional[int] = Field(default=None, foreign_key="bioma.id")


db_name = "zooapi2.db"
db_url = f"sqlite:///app/{db_name}"

engine = create_engine(db_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)

    # bioma = Bioma(name="desierto")
    # animal = Animal(name="Lagarto", edad=3, bioma=1)
    
    # with Session(engine) as session:
    #     session.add(bioma)
    #     session.add(animal)
    #     session.commit()

    # with Session(engine) as session:
    #     datos = session.exec(select(Animal).join(Bioma)).all()
    #     print(datos)
    

