from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template('base.html')

@app.route("/usuario")
@app.route("/usuario/<nombre>")
def saludar(nombre="Usuario"):
    return f"<h3>Hola, {nombre.capitalize()}, ¿cómo estás?</h3>"


@app.route("/saludar", methods=["GET", "POST"])
def decir_hola():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        return f"Hola, como estás {nombre}"

    return render_template('saludar.html')

if __name__ == "__main__":
    app.run(debug=True)