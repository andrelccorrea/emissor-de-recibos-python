# gerenciador de janelas
from kivy.uix.screenmanager import Screen
# usa StringProperty para carregar dados dinamicamente
from kivy.properties import StringProperty, ListProperty
# banco de dados
import sqlite3
import banco_sqlite as banco
# listagem
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
# mensagens em popup
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# usado para carregar as definições do arquivo .kv
from kivy.lang.builder import Builder
# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Builder.load_string(open("tela_consultar_pagadores.kv",encoding="utf-8").read())

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass

class TableHeaderLabel(RecycleDataViewBehavior, Label):
    pass

class TableRowLabel(RecycleDataViewBehavior, Label):
    pass

class TelaConsultarPagadores(Screen):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(TelaConsultarPagadores, self).__init__(**kwargs)
        self.retornar_pagadores()

    def retornar_pagadores(self):
        connection = sqlite3.connect("recibos.db")
        cursor = connection.cursor()

        cursor.execute("SELECT nome,cpf,telefone FROM pagadores ORDER BY pagador_id ASC")
        rows = cursor.fetchall()

        self.data_items = []
        
        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)