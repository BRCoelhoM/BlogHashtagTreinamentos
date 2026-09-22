from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from BlogHashtagTreinamentos.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username =  StringField('Nome do Usuário', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField ('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError ('E-mail já cadastrado')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembra_dados = BooleanField('Lembrar de Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png','jpeg'])])

    curso_python = BooleanField('Python Impressionador')
    curso_sql =BooleanField('SQL Impressionador')
    curso_excel = BooleanField('Excel Impressionador')
    curso_powerbi = BooleanField('Power BI Impressionador')
    curso_vba = BooleanField('Vba Impressionador')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self,email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                 raise ValidationError ('Já existe um usuário com este email')


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired(), Length(min=2, max=140)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')