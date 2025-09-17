from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


usuarios_db = {
    1: {
        "id": 1,
        "username": "admin",
        "password": "admin123"
    }
}


class UserLogin(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod    
    def get(user_id):
        user_data = usuarios_db.get(int(user_id))
        if user_data:
            return UserLogin(
                id = user_data["id"],
                username = user_data["username"],
                password = user_data["password"]
            )
        return None
    
    @staticmethod    
    def get_by_username(username):
        for user_data in usuarios_db.values():
            if user_data["username"] == username:
                return UserLogin(
                    id = user_data["id"],
                    username = user_data["username"],
                    password = user_data["password"]
                )
        return None

    def check_password(self, password):
        return self.password == password
    

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    prioridad = db.Column(db.Integer, nullable=False, default=3)
    completada = db.Column(db.Boolean, default=False)

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'titulo': self.titulo,
    #         'prioridad': self.prioridad,
    #         'completada': self.completada
    #     }
