# Checklist

## 1. Estructura del Proyecto
Crear la estructura del proyecto (app, app/controllers, app/database, app/models, app/routes, tests)

> IaC -> gitignore, env, requerimientos, directorios y archivos \_\_init__

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

### Para My SQL
```python
    # MYSQL Configuration
    # DB_CONNECTION=mysql
    # DB_HOST=127.0.0.1
    # DB_PORT=3306
    # DB_DATABASE=homestead
    # DB_USERNAME=homestead
    # DB_PASSWORD=secret
    ####
    #Ensamblar en python -> f"{DB_CONNECTION}+mysqlclient://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    ####
```