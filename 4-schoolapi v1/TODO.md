# TODO: Integrando MongoDB

Aquí he puesto los pasos a llevar a cabo para trabajar con MongoDB en FastAPI con la librería que hemos elegido.

## 1. Instalar dependencias

Crear .venv y activar.

Hay que instalar `fastapi[standard]`, `motor`, `beanie` y `python-decouple` para prod y `black`, `faker` y `pytest` para dev.

## 2. Create and Configure Environment Variables

Crear un archivo `.env` en la raíz del proyecto con la siguiente línea:

```
MONGO_URL=mongodb://localhost:27017
```

## 3. Base de datos

- Importaciones
- URL de conexión
- Modelo de datos con Document, y class Settings con el nombre de colección
- init (cliente, database, init_beanie con modelos)
- lifespan (asynccontextmanager) para integrar con FastAPI