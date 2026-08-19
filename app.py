from flask import Flask
from flask_login import LoginManager
from models import db, Usuario

app = Flask(__name__)

# --- CONFIGURAÇÕES DO APP ---
app.config['SECRET_KEY'] = 'chave_secreta_musicstream_123' # Obrigatório para sessões
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