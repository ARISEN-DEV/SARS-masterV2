from flask import g, Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuario import Usuario
from utils.db import db
import bcrypt


auth = Blueprint("auth", __name__)
seed = bcrypt.gensalt()


@auth.route("/")
def index():

    return render_template('index.html')

# @auth.route("/index", methods=["POST", "GET"])
# def obtener_usuarios_por_nombre_clave(email, password):
#     obtener_usuario_sql = f"""
#             SELECT id, email 
#             FROM Usuarios
#             WHERE email='{email}' and password='{password}' 
#         """
#     bd = BaseDeDatos()
#     return [{"id": registro[0],
#             "nombre": registro[1],
#             "rol": registro[2]
#             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]

@auth.route("/index", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.pop('usuario_id', None)

        email = request.form["email"]
        password = request.form["password"]
        # password_encode = password.encode("utf-8")
        # password_encrypted = bcrypt.hashpw(password_encode, seed)
        usuario = db.session.query(Usuario).filter_by(email=email).first()

        if email==usuario.email and password==usuario.password:
            session['usuario_id'] = usuario.id
            flash("Me alegra que estes aqui")
            return redirect(url_for('auth.dashboard'))
        
        else:
            flash('El usuario no existe')
            return redirect(url_for('auth.login'))
        
    return render_template('index.html')

@auth.route("/registrar", methods=["POST", "GET"])
def registrar():
    if request.method == "POST":
        session.pop('usuario_id', None)

        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]
        # password_encode = password.encode("utf-8")
        # password_encrypted = bcrypt.hashpw(password_encode, seed)
        usuario = db.session.query(Usuario).filter_by(email=email).first()
        
        # if email==usuario.email and password==usuario.password:
        #     flash("Las credenciales ya estan siendo usadas")
        #     return redirect(url_for('auth.login'))

        new_user = Usuario(email, password, nombre)
        db.session.add(new_user)
        db.session.commit()

        flash("Usuario creado satisfactoriamente")
        
        return redirect(url_for("auth.login"))
    return render_template('registrar.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.index'))

@auth.route('/dashboard')
def dashboard():
        return render_template('dashboard.html')