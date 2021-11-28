from utils.db import db


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    medida = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    vencimiento = db.Column(db.String(100))
    proveedor = db.Column(db.String(100))
    

    def __init__(self, nombre, cantidad, medida, precio, vencimiento, proveedor):
        self.nombre = nombre
        self.cantidad = cantidad
        self.medida = medida
        self.precio = precio
        self.vencimiento = vencimiento
        self.proveedor = proveedor
