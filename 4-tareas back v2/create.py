import os

dependencies = ["fastapi[standard]", "sqlmodel"]
dev_dependencies = ["black", "pytest", "faker"]
gitignore = [".venv", ".env", "create.py", "\n"]
ejemplo_env = f"# MYSQL Configuration\nDB_CONNECTION=mysql\nDB_HOST=\nDB_PORT=3306\nDB_DATABASE=\nDB_USERNAME=\nDB_PASSWORD=\n"
dir_raiz = "app"
folders = [
    f"{dir_raiz}/controllers",
    f"{dir_raiz}/models",
    f"{dir_raiz}/database",
    f"{dir_raiz}/routes",
    "tests"
]

# Función para crear requerimientos e instalarlos
def create_and_install_requirements():
    # Asegurarnos de utilizar la última versión de pip (en linux o macOS puede cambiar)
    os.system("python -m pip install --upgrade pip")

    with open("requirements.txt", "w") as file:
        for dep in dependencies:
            file.write(dep + "\n")        
        print("[SUCCESS]: requirements.txt created")

    with open("dev-requirements.txt", "w") as file:
        for dep in dev_dependencies:
            file.write(dep + "\n")        
        print("[SUCCESS]: dev-requirements.txt created")

    os.system("pip install -r requirements.txt")
    os.system("pip install -r dev-requirements.txt")

    print("[SUCCESS]: Todos los requerimientos han sido instalados")

# Función para crear envs
def create_envs():
    with open(".env", "w") as f: pass
    print("[SUCCESS]: .env creado correctamente")

    with open(".env.example", "w") as f:
        f.write(ejemplo_env)
    print("[SUCCESS]: .env.example creado correctamente")

# Función para gitignore
def create_gitignore():
    with open(".gitignore", "w") as file:
        for ignore in gitignore:
            file.write(ignore + "\n")
    print("[SUCCESS]: .gitignore creado correctamente")

# Función para directorios y __init__.py
def create_folders_and_inits():
    for folder in folders:
        os.makedirs(folder)
        if dir_raiz in folder:
            with open(f"{folder}/__init__.py", "w") as f: pass

    with open(f"{dir_raiz}/main.py", "w") as file: pass
    
    print("[SUCCESS]: Estructura de directorios creada correctamente")

if __name__ == "__main__":
    create_and_install_requirements()
    create_envs()
    create_gitignore()
    create_folders_and_inits()