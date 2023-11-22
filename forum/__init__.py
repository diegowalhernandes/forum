from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcf5c2e692aa78a1e79f7f74a42863eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'


database = SQLAlchemy(app)

from forum import routes