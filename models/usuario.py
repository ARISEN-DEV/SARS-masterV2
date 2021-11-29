from utils.db import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nombre = db.Column(db.String(100))

    def __init__(self, email, password, nombre):
        self.email = email
        self.password = password
        self.nombre = nombre
        