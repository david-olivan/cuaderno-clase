from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


usuarios_db = {
    1: {
        "id": 1,
        "username": "admin",
        "password": "admin123"
    }
}


class UserLogin(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod    
    def get(user_id):
        user_data = User.query.get(user_id)
        if user_data:
            return UserLogin(
                id = user_data.id,
                username = user_data.username
            )
        return None
    
    @staticmethod    
    def get_by_username(username):
        user_data = User.query.filter(User.username.contains(username)).first()
        if user_data:
            return UserLogin(
                id = user_data.id,
                username = user_data.username
                )
        return None   


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    tareas = db.relationship('Tareas', backref='propietario', lazy=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)


class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    prioridad = db.Column(db.Integer, nullable=False, default=3)
    completada = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, foreign_key='user.id')

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'titulo': self.titulo,
    #         'prioridad': self.prioridad,
    #         'completada': self.completada
    #     }
