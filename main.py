# gerenciador de janelas
from kivy.uix.screenmanager import ScreenManager
# classe principal do aplicativo
from kivy.app import App
# usado para carregar as fontes
from kivy.core.text import LabelBase
#carrega as telas de seus respectivos arquivos
from tela_inicial import TelaInicial
from tela_configuracoes import TelaConfiguracoes
from tela_cadastrar_pagadores import TelaCadastrarPagadores
from tela_consultar_pagadores import TelaConsultarPagadores
from tela_cadastrar_itens import TelaCadastrarItens
from tela_consultar_itens import TelaConsultarItens
from tela_emitir_recibo import TelaEmitirRecibo

# cria o gerenciador de telas e adiciona as telas
# atenção aos nomes passados como parâmetro, pois
# são usados no arquivo gui.kv para navegação
sm = ScreenManager()
sm.add_widget(TelaInicial(name='tela_inicial'))
sm.add_widget(TelaConfiguracoes(name='tela_configuracoes'))
sm.add_widget(TelaCadastrarPagadores(name='tela_cadastrar_pagador'))
sm.add_widget(TelaConsultarPagadores(name='tela_consultar_pagadores'))
sm.add_widget(TelaCadastrarItens(name='tela_cadastrar_itens'))
sm.add_widget(TelaConsultarItens(name='tela_consultar_itens'))
sm.add_widget(TelaEmitirRecibo(name='tela_emitir_recibo'))

class Main(App):
    def build(self):
        # carrega as fontes (fonte free para uso comercial / baixei de fontsquirrel.com)
        LabelBase.register(name = "AlexBrush", fn_regular = "fonts/AlexBrush-Regular.ttf")
        self.title = "Emissor de Recibos"
        self.icon = "img/icone.png"
        return sm

if __name__ == '__main__':
    Main().run()