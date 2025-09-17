from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_required, current_user, login_user, logout_user

from forms import NuevaTarea, LoginForm
from models import UserLogin, db, Tareas, User

app = Flask(__name__)
app.secret_key = "clave_secreta"

csrf = CSRFProtect(app)

# Configuración de CSRF
app.config['WTF_CSRF_TIME_LIMIT'] = 3600
app.config['WTF_CSRF_ENABLED'] = True
# Configuración de BBDD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi-base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # type: ignore
login_manager.login_message = "Porfa, logueate que si no, no te dejo pasar"
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return UserLogin.get(user_id)

@app.route("/")
@login_required
def inicio():
    # Para conseguir query arguments
    # query = request.args.get('nombre', "")
    return render_template("tareas/lista.html", tareas=Tareas.query.all())


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Ya estás logueado", 'info')
        return redirect(url_for('inicio'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data

        user_data = User.query.filter(User.username.contains(username)).first()
        if user_data and user_data.check_password(password):
            usuario_actual = UserLogin(
                id=user_data.id,
                username=user_data.username
            )
            login_user(usuario_actual, remember=remember)
            flash(f'Bienvenido a tus tareas, {usuario_actual.username.capitalize()}', 'info')

            return redirect(url_for('inicio'))
        else:
            flash('El usuario o contraseña no es válido', 'error')

    return render_template('auth/login.html', form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("Ya estás logueado", 'info')
        return redirect(url_for('inicio'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if User.query.filter(User.username.contains(username)).first():
            flash("El usuario ya existe, elige otro nombre", "error")
            return render_template('auth/register.html', form=form)

        nuevo_usuario = User(
            username=username, # type: ignore
            password=User.set_password(password) # type: ignore
        )

        print(nuevo_usuario)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash("Usuario creado correctamente", "success")
        return redirect(url_for('login'))
    
    return render_template('auth/register.html', form=form)

@app.route("/logout")
def logout():
    nombre = current_user.username
    logout_user()
    flash(f'Hasta luego, {nombre.capitalize()}', 'info')
    return redirect(url_for('login'))

@app.route("/tareas/nueva", methods=["GET", "POST"])
@login_required
def nueva_tarea():
    form = NuevaTarea()

    '''
    if request.method == "POST":
        nuevo_titulo: str = request.form.get("titulo").strip()  # type: ignore
        if nuevo_titulo:
            nuevo_id = max([t["id"] for t in tareas]) + 1 if tareas else 1
            tareas.append({"id": nuevo_id, "titulo": nuevo_titulo, "completada": False})
            flash("Tarea añadida", "success")
            return redirect(url_for("inicio"))
        else:
            flash("El título es obligatorio", "error")'''
    
    if form.validate_on_submit():
        nuevo_titulo = form.titulo_tarea.data
        prioridad = form.prioridad.data
        # nuevo_id = max([t["id"] for t in tareas]) + 1 if tareas else 1
        # tareas.append({
        #     "id": nuevo_id,
        #     "titulo": nuevo_titulo, 
        #     "prioridad": prioridad,
        #     "completada": False
        #     })
        nueva_tarea = Tareas(
            titulo=nuevo_titulo, # type: ignore
            prioridad=prioridad # type: ignore
            )
        db.session.add(nueva_tarea)
        db.session.commit()
        flash("Tarea añadida", "success")
        return redirect(url_for("inicio"))

    return render_template("tareas/nueva.html", form=form)


@app.route("/tareas/<int:id>/completar")
def completar_tarea(id):
    # for tarea in tareas:
    #     if tarea["id"] == id:
    #         tarea["completada"] = not tarea["completada"]
    #         flash("Tarea modificada", "success")

    tarea: Tareas | None = Tareas.query.get(id)
    if tarea:
        tarea.completada = not tarea.completada
        db.session.commit()
        flash("Tarea modificada", "success")
    else:
        flash("No existe una tarea con ese id", "error")
    return redirect(url_for("inicio"))


@app.route("/tareas/<int:id>/eliminar")
def eliminar_tarea(id):
    # for tarea in tareas:
    #     if tarea["id"] == id:
    #         tareas.remove(tarea)
    #         flash("Tarea eliminada", "error")
    tarea_eliminar: Tareas | None = Tareas.query.get(id)
    if tarea_eliminar:
        db.session.delete(tarea_eliminar)
        flash("Tarea eliminada correctamente", "success")
    else:
        flash("No existe una tarea con ese id", "error")
    return redirect(url_for("inicio"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
