from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcf5c2e692aa78a1e79f7f74a42863eb'
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///forum.db'

database = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucessono e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)