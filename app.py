import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
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

# --- ROTAS DA APLICAÇÃO ---

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and check_password_hash(usuario.senha_hash, senha):
            login_user(usuario)
            return redirect(url_for('home'))
        else:
            flash('E-mail ou senha incorretos.')
            
    return render_template('login.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")

        if senha != confirmar_senha:
            return render_template("cadastro.html", erro="As senhas não coincidem!")

        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            return render_template("cadastro.html", erro="Este e-mail já está cadastrado!")

        senha_criptografada = generate_password_hash(senha)
        novo_usuario = Usuario(nome=nome, email=email, senha_hash=senha_criptografada)

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("confirmacao"))

    return render_template("cadastro.html")

@app.route("/confirmacao")
def confirmacao():
    return render_template("confirmacao.html")

@app.route("/home")
@login_required
def home():
    return render_template("home.html", usuario=current_user.nome)

@app.route('/buscar', methods=['GET'])
@login_required
def buscar():
    query = request.args.get('q', '')
    resultados = []

    if query:
        try:
            url = f"https://discoveryprovider.audius.co/v1/tracks/search?query={query}&app_name=MUSICSTREAM"
            resposta = requests.get(url, timeout=5)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                resultados = dados.get('data', [])
        except Exception as e:
            print(f"Erro ao buscar na API da Audius: {e}")

    return render_template('buscar.html', resultados=resultados, query=query, usuario=current_user.nome)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)