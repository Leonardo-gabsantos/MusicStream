from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicstream.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo do Usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

# Criar a tabela no banco automaticamente
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        # 1. Busca o usuário pelo e-mail
        usuario = Usuario.query.filter_by(email=email).first()

        # 2. Verifica se existe e se a senha está correta
        if usuario and check_password_hash(usuario.senha_hash, senha):
            return f"<h1>Bem-vindo, {usuario.nome}! Login realizado com sucesso.</h1>"
        else:
            erro = "E-mail ou senha incorretos."

    return render_template("login.html", erro=erro)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")

        # 1. Validação de senhas iguais
        if senha != confirmar_senha:
            return render_template("cadastro.html", erro="As senhas não coincidem!")

        # 2. Validação de e-mail existente
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            return render_template("cadastro.html", erro="Este e-mail já está cadastrado!")

        # 3. Criptografa a senha e grava no banco
        senha_criptografada = generate_password_hash(senha)
        novo_usuario = Usuario(nome=nome, email=email, senha_hash=senha_criptografada)

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("confirmacao"))

    return render_template("cadastro.html")

@app.route("/confirmacao")
def confirmacao():
    return render_template("confirmacao.html")

if __name__ == "__main__":
    app.run(debug=True)