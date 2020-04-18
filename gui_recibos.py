from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Window.size = (600,300)
Builder.load_string(open("gui.kv",encoding="utf-8").read())

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
        self.icon = "icone.png"
        return sm

if __name__ == '__main__':
    Main().run()