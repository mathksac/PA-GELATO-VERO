from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
import re

app = Flask(__name__)
CORS(app, origins="*")

BANCO = os.path.join(os.path.dirname(__file__), "clientes.db")

def conectar():
    return sqlite3.connect(BANCO)

def criar_tabela():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefone TEXT
            )
        """)

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({"mensagem": "API Gelato Vero funcionando!"})

@app.route("/cadastro", methods=["POST"])
def cadastrar():
    dados = request.get_json(silent=True) or {}
    nome = dados.get("nome", "").strip()
    email = dados.get("email", "").strip().lower()
    telefone = dados.get("telefone", "").strip()

    if len(nome) < 2 or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return jsonify({"erro": "Informe um nome e um e-mail válido."}), 400

    try:
        with conectar() as conexao:
            conexao.execute(
                "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone)
            )
        return jsonify({"mensagem": "Cadastro realizado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado."}), 409

criar_tabela()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
