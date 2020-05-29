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
Builder.load_string(open("tela_configuracoes.kv",encoding="utf-8").read())

# usado para instanciar os TextInputs
from kivy.uix.textinput import TextInput

class TextInputNome(TextInput):
    def on_parent(self, widget, parent):
        self.focus = True

class TextInputCpf(TextInput):
    pass

class TextInputEndereco(TextInput):
    pass

class TextInputBairro(TextInput):
    pass

class TextInputCidade(TextInput):
    pass

class TextInputUf(TextInput):
    pass

class TextInputTelefone(TextInput):
    pass

class TelaConfiguracoes(Screen):
    def build(self):
        return TextInputNome()