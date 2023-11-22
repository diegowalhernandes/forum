from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcf5c2e692aa78a1e79f7f74a42863eb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

database = SQLAlchemy(app)

# Importe seus modelos aqui
from forum.models import Usuario  # Certifique-se de substituir 'Usuario' pelo nome real do seu modelo

# Crie as tabelas antes de executar o aplicativo
with app.app_context():
    database.create_all()

# Importe suas rotas aqui
from forum import routes
