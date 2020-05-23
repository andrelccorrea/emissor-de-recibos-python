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
Builder.load_string(open("tela_inicial.kv",encoding="utf-8").read())

class TelaInicial(Screen):
    # carregar do banco
    nome_do_recebedor = StringProperty("Nome do Recebedor")
    # carregar conforme configuração
    logo = StringProperty("img/inicio.png")