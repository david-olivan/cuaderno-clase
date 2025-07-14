# Checklist

## 1. Estructura del Proyecto
Crear la estructura del proyecto (api, api/controllers, api/database, api/models, api/routes, tests)

## 2. Dependencias
Crear `requirements.txt` y `dev-requirements.txt` con el siguiente contenido:

**`requirements.txt`**

```
fastapi[standard]
sqlmodel
```

**`dev-requirements.txt`**

```
black
pytest
faker
```
## 3. Instalar Dependencias
Crear un entorno virtual e instalar las dependencias.

## 4. Aplicación FastAPI
Crear el archivo principal de la aplicación FastAPI `src/main.py`.

Explicar Middleware, implementarlo para explicar cómo securizar la api (importar CORSMiddleware, establecer origins, app.add_middleware, con los 4 allows origins, credentials, methods y headers).

## 5. Modelos
Crear los esquemas de Pydantic en `src/models.py`.
- Animal
- AnimalCreate
- AnimalResponse

## 6. Rutas de la API
Crear las rutas de la API en `src/routes/animals.py`:

## 7. Controladores de la API
Crear los controladores de la API en `src/controllers/animals.py`:

## 8. Configuración de la Base de Datos
Crear la conexión a la base de datos en `src/db/database.py`.
Crear un seeder para la base de datos en `src/utils/seeder.py`.