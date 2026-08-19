from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)


class Curtida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    track_id = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    artista = db.Column(db.String(255), nullable=False)
    url_audio = db.Column(db.String(500), nullable=False)
    capa_url = db.Column(db.String(500), nullable=True)
    criada_em = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('curtidas', lazy=True))
    __table_args__ = (db.UniqueConstraint('usuario_id', 'track_id', name='uq_usuario_track'),)