"""Site acadêmico Gelato Vero: Flask, HTML e SQLite, sem bibliotecas de frontend."""
import re
import sqlite3
from datetime import date
from pathlib import Path
import click
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DATABASE'] = str(Path(__file__).with_name('banco.db'))
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024


def conectar():
    # A conexão é fechada após cada operação.
    banco = sqlite3.connect(app.config['DATABASE'])
    banco.row_factory = sqlite3.Row
    return banco


def criar_banco():
    banco = conectar()
    banco.execute('''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, cpf TEXT NOT NULL UNIQUE,
        nascimento TEXT NOT NULL, email TEXT NOT NULL,
        telefone TEXT NOT NULL, cidade TEXT NOT NULL
    )''')
    banco.commit()
    banco.close()


def cpf_valido(cpf):
    # O CPF tem 11 números e dois dígitos verificadores.
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False
    for tamanho in (9, 10):
        soma = sum(int(cpf[i]) * (tamanho + 1 - i) for i in range(tamanho))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[tamanho]):
            return False
    return True


def validar(dados):
    erros = []
    for campo in ('nome', 'cpf', 'nascimento', 'email', 'telefone', 'cidade'):
        if not dados[campo]:
            erros.append('Preencha todos os campos obrigatórios.')
            return erros
    if len(dados['nome']) > 100 or len(dados['nome'].split()) < 2:
        erros.append('Informe seu nome completo, com até 100 caracteres.')
    if not cpf_valido(dados['cpf']):
        erros.append('Informe um CPF válido.')
    try:
        nascimento = date.fromisoformat(dados['nascimento'])
        if nascimento > date.today():
            erros.append('A data de nascimento não pode estar no futuro.')
    except ValueError:
        erros.append('Informe uma data de nascimento válida.')
    if len(dados['email']) > 255 or not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', dados['email']):
        erros.append('Informe um e-mail válido.')
    if len(dados['telefone']) not in (10, 11):
        erros.append('Informe um telefone com DDD e 10 ou 11 números.')
    if len(dados['cidade']) > 100:
        erros.append('A cidade deve ter até 100 caracteres.')
    return erros


@app.route('/')
def inicio():
    return render_template('index.html', titulo='O verdadeiro sabor da natureza')


@app.route('/sabores')
def sabores():
    return render_template('sabores.html', titulo='Nossos sabores')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre nós')


@app.route('/contato')
def contato():
    # O formulário não simula mensagens: envio desativado até haver um destino oficial.
    return render_template('contato.html', titulo='Contato')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    dados = {campo: '' for campo in ('nome', 'cpf', 'nascimento', 'email', 'telefone', 'cidade')}
    erros = []
    sucesso = False
    status = 200
    if request.method == 'POST':
        for campo in dados:
            dados[campo] = request.form.get(campo, '').strip()
        dados['cpf'] = re.sub(r'\D', '', dados['cpf'])
        dados['telefone'] = re.sub(r'\D', '', dados['telefone'])
        erros = validar(dados)
        if erros:
            status = 400
        else:
            banco = conectar()
            try:
                # Os valores são parâmetros, nunca concatenados ao SQL.
                banco.execute('''INSERT INTO clientes
                    (nome, cpf, nascimento, email, telefone, cidade)
                    VALUES (?, ?, ?, ?, ?, ?)''', tuple(dados.values()))
                banco.commit()
                sucesso = True
                dados = {campo: '' for campo in dados}
            except sqlite3.IntegrityError:
                erros.append('Este CPF já está cadastrado.')
                status = 409
            except sqlite3.Error:
                erros.append('Não foi possível salvar o cadastro. Tente novamente.')
                status = 500
            finally:
                banco.close()
    return render_template('cadastro.html', titulo='Cadastro de clientes', dados=dados,
                           erros=erros, sucesso=sucesso), status


@app.cli.command('listar-clientes')
def listar_clientes():
    """Consulta local: os dados pessoais nunca são expostos em uma página pública."""
    criar_banco()
    banco = conectar()
    clientes = banco.execute('SELECT * FROM clientes ORDER BY id DESC').fetchall()
    for cliente in clientes:
        click.echo(dict(cliente))
    click.echo(f'Total de clientes: {len(clientes)}')
    banco.close()


criar_banco()

if __name__ == '__main__':
    # Apenas na máquina local. Não ativar debug em um servidor público.
    app.run(host='127.0.0.1', port=5000)
