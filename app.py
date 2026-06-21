from flask import Flask, render_template, request, jsonify # type: ignore
import mysql.connector # type: ignore

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LISTAR ----------------
@app.route("/produtos", methods=["GET"])
def listar_produtos():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[SENHA]",
        database="projeto_python"
    )

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(produtos)


# ---------------- CRIAR ----------------
@app.route("/produtos", methods=["POST"])
def criar_produto():

    dados = request.json

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[SENHA]",
        database="projeto_python"
    )

    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s)",
        (dados["nome"], dados["preco"])
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Produto criado"})


# ---------------- DELETAR ----------------
@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir_produto(id):

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="[SENHA]",
        database="projeto_python"
    )

    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Produto excluído"})


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)