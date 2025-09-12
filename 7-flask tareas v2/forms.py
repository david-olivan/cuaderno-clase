from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange

class NuevaTarea(FlaskForm):
    titulo_tarea = StringField(
        "Título de la tarea:",
        validators=[
            DataRequired(message="El título de la tarea es obligatorio"),
            Length(min=3, max=50, message="La longitud del título tiene que estar entre 3 y 50")
        ],
        render_kw = {"autofocus": True}
    )

    prioridad = IntegerField(
        "Prioridad de la tarea",
        validators=[
            DataRequired(message="Es necesario poner una prioridad"),
            NumberRange(min=1, max=3, message="La prioridad puede estar entre 1 y 3")
        ]
    )

    submit = SubmitField("Guardar Tarea")


class LoginForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[
            DataRequired(message="El usuario es obligatorio"),
            Length(min=3, max=25, message="El usuario no es válido")
        ]
    )

    password = PasswordField(
        "Contraseña:",
        validators=[DataRequired(message="La contraseña es obligatoria")]
    )

    remember = BooleanField("Recordarme")

    submit = SubmitField("Login")