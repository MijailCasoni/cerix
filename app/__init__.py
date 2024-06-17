from flask import Flask
from .models import db  # Importar db desde models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/cerix'  # Corregido
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para evitar mensajes deprecados

    db.init_app(app)  # Inicializar la base de datos con la aplicación

    # Registrar blueprints aquí
    from app.routes import main
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()  # Crear tablas en la base de datos
    return app