import kivy
kivy.require('1.11.1')

# a classe principal do aplicativo deve estender a classe App
from kivy.app import App
# widgets usados para trabalhar com múltiplas telas
from kivy.uix.screenmanager import ScreenManager, Screen
# widgets usados para alterar as cores de fundo dos componentes e telas
from kivy.graphics import Color, Rectangle
# demais widgets que serão usados no projeto
from kivy.uix.label import Label

class TelaInicial(Screen):

    # necessário sobrescrever o método init da classe Screen, passando os argumentos
    # para que os widgets possam ser adicionados e configurados na inicialização
    def __init__(self,**kwargs):
        super(TelaInicial, self).__init__(**kwargs)
        # widgets
        self.add_widget(Label(text='Teste telas', color=[1,0,0,1]))

        # define a cor da tela
        with self.canvas.before:
            Color(0,1,0,1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
        # vincula o retângulo colorido para que seja redimensionado juntamente com a tela do app
        self.bind(size=self._update_rect, pos=self._update_rect)
    
    # atualiza o tamanho e posição do retângulo
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaInicial(name='tela_inicial'))
        return sm

if __name__ == '__main__':
    MyApp().run()