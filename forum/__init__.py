from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcf5c2e692aa78a1e79f7f74a42863eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from forum.models import Usuario 


with app.app_context():
    database.create_all()

# Importe suas rotas aqui
from forum import routes
