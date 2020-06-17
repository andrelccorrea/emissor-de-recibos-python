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
Builder.load_string(open("tela_cadastrar_pagadores.kv",encoding="utf-8").read())

# banco de dados
import sqlite3
import banco_sqlite as banco

# mensagens em popup
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# campos personalizados
from kivy.uix.textinput import TextInput

# inputs
class TextInputNome(TextInput):
    def on_parent(self, widget, parent):
        self.focus = True

class CPFInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if not substring.isnumeric() or len(self.text) > 13:
            return
        if len(self.text) == 3:
            substring = "." + substring
        elif len(self.text) == 7:
            substring = "." + substring
        elif len(self.text) == 11:
            substring = "-" + substring 
        return super().insert_text(substring, from_undo=from_undo)

class TelefoneInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if not substring.isnumeric() or len(self.text) > 12:
            return
        if len(self.text) == 0:
            substring = "(" + substring
        elif len(self.text) == 3:
            substring = ")" + substring
        return super().insert_text(substring, from_undo=from_undo)

class TelaCadastrarPagadores(Screen):
    def exibir_popup(self, titulo, mensagem):
        pop = Popup(title=titulo,
                    content=Label(text=mensagem),
                    size_hint=(None, None), size=(350, 120))
        pop.open()

    def validar_campos(self):
        if not self.ids.txt_nome.text:
            self.exibir_popup('Campo inválido','Preencha corretamente o nome.')        
            return False
        elif not self.ids.txt_cpf.text:
            self.exibir_popup('Campo inválido','Preencha corretamente o CPF.')        
            return False
        return True

    def cadastrar_pagador(self):
        # abre uma conexão com o banco
        conexao = sqlite3.connect("recibos.db")

        if banco.buscar_pagador(conexao, self.ids.txt_cpf.text) == 0:
            # junta os dados do form
            dados = [self.ids.txt_nome.text, self.ids.txt_cpf.text, self.ids.txt_telefone.text]
            # grava os dados
            banco.cadastrar_pagador(conexao, dados)
            # limpa os campos
            self.ids.txt_nome.text = ""
            self.ids.txt_cpf.text = ""
            self.ids.txt_telefone.text = ""
            # fecha a conexão com o banco
            conexao.close()
            self.exibir_popup('Cadastro','Pagador cadastrado com sucesso!')
        else:
            self.exibir_popup('Atenção','Pagador já cadastrado!')
        return