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
    def exibir_popup(self, titulo, mensagem):
        pop = Popup(title=titulo,
                    content=Label(text=mensagem),
                    size_hint=(None, None), size=(350, 120))
        pop.open()

    def validar_campos(self):
        if not self.ids.txt_descricao.text:
            self.exibir_popup('Campos inválidos','Preencha corretamente a descrição do item.')        
            return False
        elif not self.ids.txt_preco.text or float(self.ids.txt_preco.text) <= 0:
            self.exibir_popup('Campos inválidos','Preencha corretamente o preço do item.')        
            return False
        return True

    def cadastrar_item(self):
        # abre uma conexão com o banco
        conexao = sqlite3.connect("recibos.db")
        # junta os dados do form
        dados = [self.ids.txt_descricao.text, self.ids.txt_preco.text]
        # grava os dados
        banco.cadastrar_item(conexao, dados)
        # limpa os campos
        self.ids.txt_descricao.text = ""
        self.ids.txt_preco.text = ""
        # fecha a conexão com o banco
        conexao.close()
        self.exibir_popup('Cadastro','Item cadastrado com sucesso!')
        #self.super(TelaConsultarItens, self).atualizar_lista()
        return