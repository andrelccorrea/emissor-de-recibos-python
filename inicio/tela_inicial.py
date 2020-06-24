# gerenciador de janelas
from kivy.uix.screenmanager import Screen
# usa StringProperty para carregar dados dinamicamente
from kivy.properties import StringProperty
# banco de dados
import sqlite3
# funções de manipulação do banco de dados
import banco_sqlite as banco

# usado para carregar as definições do arquivo .kv
from kivy.lang.builder import Builder
# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Builder.load_string(open("inicio/tela_inicial.kv",encoding="utf-8").read())

class TelaInicial(Screen):

    nome_do_recebedor = StringProperty("Nome do Recebedor")

    logo = StringProperty("img/inicio.png")

    def carregar_nome_do_recebedor(self):
        conexao = sqlite3.connect("recibos.db")
        recebedor = banco.retornar_recebedor(conexao)
        if recebedor:
            self.nome_do_recebedor = recebedor[1]

    def on_enter(self):
        self.carregar_nome_do_recebedor()