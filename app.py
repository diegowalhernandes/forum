from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta


app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcf5c2e692aa78a1e79f7f74a42863eb'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html')

@app.route("/login")
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)