from flask import Flask
from flask_login import LoginManager
from models import db, Usuario
import os
from pathlib import Path


def carregar_env():
    caminho_env = Path(__file__).with_name('.env')
    if not caminho_env.exists():
        return

    for linha in caminho_env.read_text(encoding='utf-8').splitlines():
        nome, separador, valor = linha.partition('=')
        if separador and nome.strip() == 'SECRET_KEY':
            os.environ.setdefault('SECRET_KEY', valor.strip().strip('"').strip("'"))


carregar_env()

app = Flask(__name__)

# --- CONFIGURAÇÕES DO APP ---
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicstream.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- INICIALIZAÇÃO DE EXTENSÕES ---
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Criar a tabela no banco 
with app.app_context():
    db.create_all()

from routes import register_routes

register_routes(app)


if __name__ == "__main__":
    app.run(debug=True)