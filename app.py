from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        # Captura os dados digitados
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")
        
        # Validação de senhas iguais
        if senha != confirmar_senha:
            #Se forem diferentes,retorna mensagem de erro.
            return render_template("cadastro.html", erro="As senhas não coincidem!")
            
        # Se deu tudo certo, redireciona para a tela de confirmação
        return redirect(url_for("confirmacao"))
        
    return render_template("cadastro.html")

@app.route("/confirmacao")
def confirmacao():
    return render_template("confirmacao.html")
# bloco para rodar o server
if __name__ == "__main__":
    app.run(debug=True)