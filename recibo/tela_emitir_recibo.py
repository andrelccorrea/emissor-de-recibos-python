# gerenciador de janelas
from kivy.uix.screenmanager import Screen
# tabela
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.behaviors import FocusBehavior
# usa StringProperty para carregar dados dinamicamente
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
# widget usado nas seleções
from kivy.uix.spinner import Spinner, SpinnerOption
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
Builder.load_string(open("recibo/tela_emitir_recibo.kv",encoding="utf-8").read())

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    pass

class TableHeaderLabel(RecycleDataViewBehavior, Label):
    pass

class TableRowLabel(RecycleDataViewBehavior, Label):
    pass

class BoxTabela(BoxLayout):
    pass

class TextInputPagador(TextInput):
    pass

class SpinnerPagadores(Spinner):
    pass

class TextInputItem(TextInput):
    pass

class SpinnerItens(Spinner):
    pass

class ButtonIncluirItem(Button):
    pass

class TelaEmitirRecibo(Screen):
    data_items = ListProperty([])

    def on_enter(self):
        self.carregar_pagadores()
        self.carregar_itens()

    def carregar_pagadores(self):

        conexao = sqlite3.connect("recibos.db")
        pagadores = banco.retornar_pagadores(conexao)
        
        if pagadores:
            # extrai apenas os ids
            nomes = [str(pagador[0]) for pagador in pagadores]
            # passa para o spinner
            self.ids.spinner_pagadores.values = nomes

        conexao.close()

        return

    def carregar_itens(self):

        conexao = sqlite3.connect("recibos.db")
        itens = banco.retornar_itens(conexao)
        
        if itens:
            # extrai apenas os ids
            descricoes = [str(item[0]) for item in itens]
            # passa para o spinner
            self.ids.spinner_itens.values = descricoes

        conexao.close()

        return

    def preencher_txt_pagador(self):
        conexao = sqlite3.connect("recibos.db")
        self.ids.txt_pagador.text = banco.buscar_pagador_pelo_id(conexao,
                                        self.ids.spinner_pagadores.text)[1]

    def preencher_txt_item(self):
        conexao = sqlite3.connect("recibos.db")
        self.ids.txt_item.text = banco.buscar_item_pelo_id(conexao,
                                        self.ids.spinner_itens.text)[1]
    
    def incluir_item_na_tabela(self):
        conexao = sqlite3.connect("recibos.db")
        item = banco.buscar_item_pelo_id(conexao, self.ids.spinner_itens.text)
        if item:
            for col in item:
                self.data_items.append(col)
            # TODO: quantidade está hardcoded, necessário checar data_items
            # e se já tiver o item, incrementar, senão, adicionar
            self.data_items.append(1)
