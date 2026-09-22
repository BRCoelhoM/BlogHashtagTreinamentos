from BlogHashtagTreinamentos import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))



class Usuario(db.Model, UserMixin):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(200), nullable=False)
    foto_perfil = db.Column(db.String(100), default='default.jpg', nullable=False)
    cursos = db.Column(db.String(500), nullable=False, default='Não Informado')
    post = db.relationship('Post', backref='autor', lazy=True)

    def contar_posts(self):
        return len(self.post)

class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
