from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Builder.load_string(open("gui.kv",encoding="utf-8").read())

# telas
class TelaInicial(Screen):
    pass

class TelaCadastroRecebedor(Screen):
    pass

class TelaCadastroPagador(Screen):
    pass

class TelaConsultaPagadores(Screen):
    pass

# cria o gerenciador de telas e adiciona as telas
# atenção aos nomes passados como parâmetro, pois
# são usados no arquivo gui.kv para navegação
sm = ScreenManager()
sm.add_widget(TelaInicial(name='tela_inicial'))
sm.add_widget(TelaCadastroRecebedor(name='tela_cadastro_recebedor'))
sm.add_widget(TelaCadastroPagador(name='tela_cadastro_pagador'))
sm.add_widget(TelaConsultaPagadores(name='tela_consultar_pagadores'))

class Main(App):

    def build(self):
        return sm

if __name__ == '__main__':
    Main().run()