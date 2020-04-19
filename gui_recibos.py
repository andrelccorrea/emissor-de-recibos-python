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
Window.size = (610,300)
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

# telas
class TelaInicial(Screen):
    pass

class TelaCadastrarRecebedor(Screen):
    pass

class TelaCadastrarPagador(Screen):
    pass

class TelaConsultarPagadores(Screen):
    pass

class TelaCadastrarItens(Screen):
    pass

class TelaConsultarItens(Screen):
    pass

class TelaEmitirRecibo(Screen):
    pass

# cria o gerenciador de telas e adiciona as telas
# atenção aos nomes passados como parâmetro, pois
# são usados no arquivo gui.kv para navegação
sm = ScreenManager()
sm.add_widget(TelaInicial(name='tela_inicial'))
sm.add_widget(TelaCadastrarRecebedor(name='tela_cadastrar_recebedor'))
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