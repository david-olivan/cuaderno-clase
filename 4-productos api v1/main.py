from fastapi import FastAPI, status, Path, Query
from typing import List, Optional
from .models import ProductoResponse, categoria, ProductoRequest, GenericResponse


app = FastAPI(
    title="Productos API",
    version="0.0.1",
    description="Another API Bites the Dust",
    contact={"name": "David en Clase", "email": "dolivan@steam.thehubfp.es"}
)

fake_productos_db = [
    ProductoResponse(
        id=1,
        name="Nothing 1 Phone",
        precio=45.87,
        description="Hola mundo",
        category=categoria.ELECTRONICA,
    ),
    ProductoResponse(
        id=2,
        name="iPhone 2",
        precio=450.87,
        description="Hola mundo",
        category=categoria.ELECTRONICA,
    ),
    ProductoResponse(
        id=3,
        name="Google Pixel 2",
        precio=4500.87,
        description="Hola mundo",
        category=categoria.ELECTRONICA,
    ),
]


@app.get("/productos", tags=["Productos"], response_model=List[ProductoResponse])
async def leer_productos(
    name: Optional[str] = Query(None, min_length=1, max_length=50)
):
    if name:
        return [
            producto
            for producto in fake_productos_db
            if name.lower() in producto.name.lower()
        ]

    return fake_productos_db


# Esto es un get usando parámetros de path
@app.get(
    "/productos/{producto_id}",
    tags=["Productos"],
    response_model=List[ProductoResponse],
)
async def leer_producto(
    producto_id: int = Path(ge=1, description="El ID del producto que quieres")
):
    return [producto for producto in fake_productos_db if producto.id == producto_id]


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
