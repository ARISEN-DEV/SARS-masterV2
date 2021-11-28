from flask import g, Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario import Usuario
from utils.db import db


auth = Blueprint("auth", __name__)


@auth.route("/")
def index():

    return render_template('index.html')

@auth.route("/index", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.pop('usuario_id', None)

        email = request.form["email"]
        password = request.form["password"]
        usuario = db.session.query(Usuario).filter_by(email=email).first()
        if usuario is not None or False:
            check = check_password_hash(usuario.password, password)
            log = email==usuario.email
            if log and check:
                session['usuario_id'] = usuario.id
                flash("Me alegra que estes aqui")
                return redirect(url_for('auth.dashboard'))
            else:
                flash('Contraseña incorrecta')
            return redirect(url_for('auth.login'))    
        
        else:
            flash('Usuario incorrecto')
            return redirect(url_for('auth.login'))
        # elif email!=usuario.email:
        #     flash('El usuario no existe')
        #     return redirect(url_for('auth.login'))
        
        # elif check_password_hash(usuario.password, password) == False:
        #     flash('El usuario no existe')
        #     return redirect(url_for('auth.login'))
        
    return render_template('index.html')

@auth.route("/registrar", methods=["POST", "GET"])
def registrar():
    if request.method == "POST":
        session.pop('usuario_id', None)

        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]
        password_encrypted = generate_password_hash(password)
        usuario = db.session.query(Usuario).filter_by(email=email).first()
        
        # if email==usuario.email and password==usuario.password:
        #     flash("Las credenciales ya estan siendo usadas")
        #     return redirect(url_for('auth.login'))

        new_user = Usuario(email, password_encrypted, nombre)
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
    if 'usuario_id' in session:
        return render_template('dashboard.html')
    else:
        flash('Por favor, inicie sesion para acceder a esta pagina')
        return redirect(url_for('auth.login'))

@auth.route('/stock')
def stock():
    if 'usuario_id' in session:
        return render_template('stock.html')
    else:
        flash('Por favor, inicie sesion para acceder a esta pagina')
        return redirect(url_for('auth.login'))