from flask import Blueprint, render_template, request, redirect, url_for
from .models import Contact, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/form')
def form():
    return render_template('form.html')


@main.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

    # Aquí podrías crear una nueva instancia de tu modelo de formulario y guardarla en la base de datos
    new_contact = Contact(name=name, email=email,
                subject=subject, message=message)

    db.session.add(new_contact)
    db.session.commit()

    # Redirige a la página de éxito después de procesar el formulario
    return redirect(url_for('main.contact_success'))


@main.route('/contact/success')
def contact_success():
    return render_template('contact_success.html', title='Success!')
