from flask_wtf import FlaskForm
from wtfforms import StringField, PasswordFielf, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
	username = StringField('Nome de Usuário', validators=[DataRequired()])
email = StringField('E-mail', validators=[DataRequired(), Email()])
senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
confirmacao_senha = PasswordField('Confirmaçã da Senha', validators=[DataRequired(), EqualTo('senha')])
botao_submit_criarconta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
	botao_submit_login = SubmitField('Fazer Login')
