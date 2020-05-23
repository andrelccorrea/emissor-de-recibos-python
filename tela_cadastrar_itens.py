# gerenciador de janelas
from kivy.uix.screenmanager import Screen
# usa StringProperty para carregar dados dinamicamente
from kivy.properties import StringProperty

# usado para carregar as definições do arquivo .kv
from kivy.lang.builder import Builder
# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Builder.load_string(open("tela_cadastrar_itens.kv",encoding="utf-8").read())

# banco de dados
import sqlite3
import banco_sqlite as banco

# mensagens em popup
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TelaCadastrarItens(Screen):
    def exibir_popup_do_erro(self):
        pop = Popup(title='Campos inválidos',
                    content=Label(text='Preencha corretamente todos os campos.'),
                    size_hint=(None, None), size=(350, 120))
        pop.open()

    def validar_campos(self):
        if not self.ids.descricao.text or not self.ids.preco.text or float(self.ids.preco.text) <= 0:
            self.exibir_popup_do_erro()        
            return False
        return True

    def cadastrar_item(self):
        # abre uma conexão com o banco
        conexao = sqlite3.connect("recibos.db")
        # junta os dados do form
        dados = [self.ids.descricao.text, self.ids.preco.text]
        # grava os dados
        banco.cadastrar_item(conexao, dados)
        # limpa os campos
        self.ids.descricao.text = ""
        self.ids.preco.text = ""
        # fecha a conexão com o banco
        conexao.close()
        return