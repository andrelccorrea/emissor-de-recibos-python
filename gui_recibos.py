# usado para bloquear o redimensionamento
from kivy.config import Config
# bloqueia o redimensionamento da janela, importante manter aqui
Config.set('graphics','resizable', False)
# gerenciador de janelas
from kivy.uix.screenmanager import ScreenManager, Screen
# classe principal do aplicativo
from kivy.app import App
# Classe para manipular a janela
from kivy.core.window import Window
# configura as medidas da janela
Window.size = (800,600)
# usado para carregar as definições do arquivo .kv
from kivy.lang.builder import Builder
# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Builder.load_string(open("gui.kv",encoding="utf-8").read())
# usado para carregar as fontes
from kivy.core.text import LabelBase
# carrega as fontes (fonte free para uso comercial / baixei de fontsquirrel.com)
LabelBase.register(name = "AlexBrush", fn_regular = "fonts/AlexBrush-Regular.ttf")
# usa StringProperty para carregar dados dinamicamente
from kivy.properties import StringProperty, ListProperty
# banco de dados
import sqlite3
import banco_sqlite as banco
# mensagens em popup
from kivy.uix.popup import Popup
from kivy.uix.label import Label
# listagem
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

# telas
class TelaInicial(Screen):
    # carregar do banco
    nome_do_recebedor = StringProperty("Nome do Recebedor")
    # carregar conforme configuração
    logo = StringProperty("img/inicio.png")

class TelaConfiguracoes(Screen):
    pass

class TelaCadastrarPagador(Screen):
    pass

class TelaConsultarPagadores(Screen):
    pass

class TelaCadastrarItens(Screen):
    def exibir_popup(self, titulo, mensagem):
        pop = Popup(title=titulo,
                    content=Label(text=mensagem),
                    size_hint=(None, None), size=(350, 120))
        pop.open()

    def validar_campos(self):
        if not self.ids.txt_descricao.text or not self.ids.txt_preco.text or float(self.ids.txt_preco.text) <= 0:
            self.exibir_popup('Campos inválidos','Preencha corretamente todos os campos.')        
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
        return

class TelaConsultarItens(Screen):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(TelaConsultarItens, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        connection = sqlite3.connect("recibos.db")
        cursor = connection.cursor()

        cursor.execute("SELECT descricao,valor FROM itens ORDER BY item_id ASC")
        rows = cursor.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)   

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass

class TableHeaderLabel(RecycleDataViewBehavior, Label):
    pass

class TableRowLabel(RecycleDataViewBehavior, Label):
    pass

class TelaEmitirRecibo(Screen):
    pass

# cria o gerenciador de telas e adiciona as telas
# atenção aos nomes passados como parâmetro, pois
# são usados no arquivo gui.kv para navegação
sm = ScreenManager()
sm.add_widget(TelaInicial(name='tela_inicial'))
sm.add_widget(TelaConfiguracoes(name='tela_configuracoes'))
sm.add_widget(TelaCadastrarPagador(name='tela_cadastrar_pagador'))
sm.add_widget(TelaConsultarPagadores(name='tela_consultar_pagadores'))
sm.add_widget(TelaCadastrarItens(name='tela_cadastrar_itens'))
sm.add_widget(TelaConsultarItens(name='tela_consultar_itens'))
sm.add_widget(TelaEmitirRecibo(name='tela_emitir_recibo'))

class Main(App):
    def build(self):
        self.title = "Emissor de Recibos"
        self.icon = "img/icone.png"
        return sm

if __name__ == '__main__':
    Main().run()