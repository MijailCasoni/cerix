from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Aquí puedes definir tus modelos
# Ejemplo de un modelo de contacto
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
