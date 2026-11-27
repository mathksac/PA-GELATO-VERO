# GELATO VERO — projeto acadêmico

Site independente, feito em HTML5, CSS3, JavaScript puro, Python, Flask e SQLite.
Não precisa de Node.js, React, TypeScript, serviços de banco ou conexão externa.

## Como executar
1. Instale Python 3.10 ou mais recente.
2. Extraia o ZIP e abra o terminal dentro da pasta `gelato-vero`.
3. Crie um ambiente virtual: `python -m venv .venv`.
4. Ative: no Windows, `.venv\Scripts\activate`; no macOS/Linux, `source .venv/bin/activate`.
5. Instale as dependências: `python -m pip install -r requirements.txt`.
6. Execute: `python app.py`.
7. Abra **http://127.0.0.1:5000** no navegador.

O arquivo `banco.db` contém a tabela `clientes` vazia na entrega. Se ele for apagado,
o Python o recria automaticamente. Nunca publique o arquivo com dados reais.

## Como funciona o cadastro
O navegador envia o formulário para `/cadastro` com POST. O Python valida nome,
CPF (incluindo os dígitos verificadores), nascimento, e-mail, telefone e cidade.
Um CPF não pode ser cadastrado duas vezes. O SQLite salva os dados com SQL
parametrizado. A página mostra sucesso somente depois da gravação no banco.

Para consultar os cadastros na sua própria máquina:
`python -m flask --app app listar-clientes`
Não existe uma lista pública de clientes, para proteger CPF e dados pessoais.
Use somente dados fictícios na apresentação escolar.

## Organização
- `app.py`: rotas, validação, conexão e comandos SQL.
- `templates/`: HTML separado, com `base.html` compartilhando cabeçalho e rodapé.
- `static/css/style.css`: cores, fontes e aparência responsiva.
- `static/js/script.js`: menu de celular e tratamento básico de campos.
- `static/img/`: logo enviada sem alteração e fotografias dos sabores.
- `test_app.py`: verificações automatizadas do cadastro.
- `banco.db`: banco SQLite criado pelo Python.

## Contato
E-mail, telefone e endereço oficiais ainda não foram informados.
O formulário de contato permanece explicitamente desativado: não simula envio.
Para inserir os contatos, altere os textos em `templates/contato.html`.

## Testes
Execute `python -m unittest test_app.py`.

## Prévia Lovable versus este projeto
A prévia online usa a tecnologia fixa do Lovable e não executa Flask.
Este ZIP é o projeto acadêmico completo e independente com as tecnologias
solicitadas. O cadastro funciona ao executar este projeto localmente.
As fotografias foram geradas para este projeto; a logo é a imagem original enviada.
