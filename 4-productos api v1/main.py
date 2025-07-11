from fastapi import FastAPI, status
from typing import List
from models import ProductoResponse, categoria, ProductoRequest, GenericResponse


app = FastAPI(
    title="Productos API", version="0.0.1", description="Another API Bites the Dust"
)


@app.get("/productos", tags=["Productos"], response_model=List[ProductoResponse])
async def leer_productos():
    return [
        ProductoResponse(
            id=1,
            name="Nothing Phone",
            precio=45.87,
            description="Hola mundo",
            category=categoria.ELECTRONICA,
        )
    ]


@app.post(
    "/productos",
    tags=["Productos"],
    response_model=GenericResponse,
    status_code=status.HTTP_201_CREATED,
)
async def nuevo_producto(producto: ProductoRequest):
    nuevo_producto = ProductoResponse(id=4, **producto.model_dump())
    return GenericResponse(
        data=[nuevo_producto], message="Producto creado correctamente"
    )
