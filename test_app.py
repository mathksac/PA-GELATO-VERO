"""Testes com dados fictícios e banco temporário, sem tocar nos clientes reais."""
import tempfile
import unittest
from pathlib import Path
from app import app, criar_banco, conectar

class CadastroTest(unittest.TestCase):
    def setUp(self):
        self.pasta = tempfile.TemporaryDirectory()
        self.anterior = app.config['DATABASE']
        app.config['DATABASE'] = str(Path(self.pasta.name) / 'teste.db')
        criar_banco()
        self.client = app.test_client()
        self.dados = dict(nome='Cliente Teste', cpf='52998224725', nascimento='2000-01-15',
                          email='teste@example.com', telefone='11999998888', cidade='São Paulo')

    def tearDown(self):
        app.config['DATABASE'] = self.anterior
        self.pasta.cleanup()

    def test_cadastro_salva_os_seis_campos(self):
        resposta = self.client.post('/cadastro', data=self.dados)
        self.assertEqual(resposta.status_code, 200)
        banco = conectar()
        cliente = banco.execute('SELECT * FROM clientes').fetchone()
        banco.close()
        self.assertIsNotNone(cliente)
        for campo, valor in self.dados.items():
            self.assertEqual(cliente[campo], valor)

    def test_cpf_duplicado_nao_cria_outro_cliente(self):
        self.client.post('/cadastro', data=self.dados)
        resposta = self.client.post('/cadastro', data=self.dados)
        self.assertEqual(resposta.status_code, 409)
        banco = conectar()
        self.assertEqual(banco.execute('SELECT COUNT(*) FROM clientes').fetchone()[0], 1)
        banco.close()

    def test_cpf_invalido_nao_e_salvo(self):
        self.dados['cpf'] = '11111111111'
        self.assertEqual(self.client.post('/cadastro', data=self.dados).status_code, 400)
        banco = conectar()
        self.assertEqual(banco.execute('SELECT COUNT(*) FROM clientes').fetchone()[0], 0)
        banco.close()

    def test_campo_obrigatorio_vazio_nao_e_salvo(self):
        self.dados['cidade'] = ''
        self.assertEqual(self.client.post('/cadastro', data=self.dados).status_code, 400)

    def test_dados_invalidos_nao_sao_salvos(self):
        for campo, valor in [('email', 'invalido'), ('nascimento', '2999-01-01'), ('telefone', '123')]:
            with self.subTest(campo=campo):
                dados = dict(self.dados)
                dados[campo] = valor
                self.assertEqual(self.client.post('/cadastro', data=dados).status_code, 400)

    def test_consulta_nao_tem_pagina_publica(self):
        self.assertEqual(self.client.get('/clientes').status_code, 404)

if __name__ == '__main__':
    unittest.main()
