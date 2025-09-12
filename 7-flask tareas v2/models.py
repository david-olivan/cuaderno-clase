from flask_login import UserMixin


usuarios_db = {
    1: {
        "id": 1,
        "username": "admin",
        "password": "admin123"
    }
}


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod    
    def get(user_id):
        user_data = usuarios_db.get(int(user_id))
        if user_data:
            return User(
                id = user_data["id"],
                username = user_data["username"],
                password = user_data["password"]
            )
        return None
    
    @staticmethod    
    def get_by_username(username):
        for user_data in usuarios_db.values():
            if user_data["username"] == username:
                return User(
                    id = user_data["id"],
                    username = user_data["username"],
                    password = user_data["password"]
                )
        return None

    def check_password(self, password):
        return self.password == password