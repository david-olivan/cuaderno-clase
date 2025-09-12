from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "clave_secreta"

tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completada": False},
    {"id": 2, "titulo": "Aprender FastAPI", "completada": True},
]


@app.route("/")
def inicio():
    # Para conseguir query arguments
    # query = request.args.get('nombre', "")
    return render_template("tareas/lista.html", tareas=tareas)


@app.route("/tareas/nueva", methods=["GET", "POST"])
def nueva_tarea():
    if request.method == "POST":
        nuevo_titulo: str = request.form.get("titulo").strip()  # type: ignore
        if nuevo_titulo:
            nuevo_id = max([t["id"] for t in tareas]) + 1 if tareas else 1
            tareas.append({"id": nuevo_id, "titulo": nuevo_titulo, "completada": False})
            flash("Tarea añadida", "success")
            return redirect(url_for("inicio"))
        else:
            flash("El título es obligatorio", "error")

    return render_template("tareas/nueva.html")


@app.route("/tareas/<int:id>/completar")
def completar_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["completada"] = not tarea["completada"]
            flash("Tarea modificada", "success")
    return redirect(url_for("inicio"))


@app.route("/tareas/<int:id>/eliminar")
def eliminar_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)
            flash("Tarea eliminada", "error")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
