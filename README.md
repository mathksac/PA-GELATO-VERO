# Gelato Vero

Sorvetes artesanais com polpas de frutas naturais — projeto acadêmico (ETEC).

O repositório guarda duas versões do mesmo site:

- `academic/gelato-vero/` — projeto acadêmico em HTML5, CSS3, JavaScript puro, Python (Flask) e SQLite. Roda na sua máquina e é a entrega principal.
- raiz do repositório (`src/`, `package.json`) — versão em React (TanStack Start), a mesma que aparece na prévia online do Lovable.

## Projeto Python (entrega principal)

```sh
cd academic/gelato-vero
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:5000. O cadastro valida nome, CPF (com dígitos verificadores), nascimento, e-mail, telefone e cidade e salva em SQLite. Não há lista pública de clientes.

Testes: `python -m unittest test_app.py`.

## Site React

```sh
npm install
npm run dev
```

## Contato

E-mail, telefone e endereço oficiais ainda não foram informados.
