from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario

app = Flask(__name__)

# Configurações do App
app.config['SECRET_KEY'] = 'chave_secreta_musicstream_123' # Obrigatorio para versoes de sessao
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicstream.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do Banco e LoginManager
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Criar a tabela no banco automaticamente
with app.app_context():
    db.create_all()

# --- ROTAS ---

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        # Valida se o usuário existe e se a senha descriptografada bate
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
@login_required # Protege a rota para apenas usuarios logados
def home():
    # Passa o nome dinamico do usuario logado na sessao
    return render_template("home.html", usuario=current_user.nome)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)