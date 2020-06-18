################################################################################

# gerenciador de janelas
from kivy.uix.screenmanager import Screen
# usa StringProperty para carregar dados dinamicamente
from kivy.properties import StringProperty
# usado para carregar as definições do arquivo .kv
from kivy.lang.builder import Builder
# banco de dados
import sqlite3
# mensagens em popup
from kivy.uix.popup import Popup
from kivy.uix.label import Label
# usado para instanciar os TextInputs
from kivy.uix.textinput import TextInput
# usado para limitar a quantidade de caracteres no textinput
from kivy.properties import NumericProperty

# funções de manipulação do banco de dados
import banco_sqlite as banco
# funções de formataçào e validação
import uteis

# carrega as definições da interface gráfica
# usei Builder.load_string com o método open, passando a codificação
# em utf-8, pois se usar o método load_file, passando direto o arquivo
# gui.kv, os acentos não são reconhecidos
Builder.load_string(open("tela_cadastrar_recebedor.kv",encoding="utf-8").read())

################################################################################
# TODO: validar campos ao passar para o próximo

#       mudar cor do campo na validação

#       preencher campos ao entrar na tela

#       criar rotina para permitir apenas 1 cadastro de recebedor, sempre sobrescrevendo ?

#       criar rotina na inicialização do programa para direcionar para esta tela caso não 
#       haja nenhum recebedor cadastrado

#       adicionar um dropdown ou list para selecionar a UF

class TextInputNome(TextInput):
    pass

class TextInputCpf(TextInput):
    def insert_text(self, substring, from_undo=False):
        if not substring.isnumeric():
            substring = ""

        texto_completo = self.text + substring
        
        if len(texto_completo) == 11:
            if uteis.validar_cpf(texto_completo):
                self.text = uteis.formatar_cpf(texto_completo)
                self.do_cursor_movement("cursor_end")
                substring = ""
        elif len(texto_completo) > 14:
            self.text = texto_completo[0:14]
            substring = ""

        return super().insert_text(substring, from_undo=from_undo)

class TextInputEndereco(TextInput):
    pass

class TextInputBairro(TextInput):
    pass

class TextInputCidade(TextInput):
    pass

class TextInputUf(TextInput):
    pass

class TextInputTelefone(TextInput):
    def insert_text(self, substring, from_undo=False):
        if not substring.isnumeric():
            substring = ""

        texto_completo = self.text + substring
        if len(texto_completo) == 11:
            self.text = uteis.formatar_telefone(texto_completo)
            self.do_cursor_movement("cursor_end")
            substring = ""
        elif len(texto_completo) > 14:
            self.text = texto_completo[0:14]
            substring = ""
        
        return super().insert_text(substring, from_undo=from_undo)

class TelaCadastrarRecebedor(Screen):
    # def __init__(self, **kwargs):
    #     if banco.retornar_recebedor(conexao) > 0:
    #     self.ids.txt_nome.text = ""
    #     super(Screen,self).__init__(**kwargs)

    def exibir_popup(self, titulo, mensagem):
        pop = Popup(title=titulo,
                    content=Label(text=mensagem),
                    size_hint=(None, None), size=(350, 120))
        pop.open()

    def validar_campos(self):
        # percorre o dicionário de ids referente aos widgets e filtra
        # os TextInputs com prefixo txt_, verificando se estão vazios
        for item in self.ids:
            if "txt_" in item:
                if not self.ids[item].text:
                    self.ids[item].focus = True
                    self.exibir_popup('Campo inválido', 'Preencha corretamente o ' + item + '.')
                    return False
        return True

    def cadastrar_recebedor(self):
        # abre uma conexão com o banco
        conexao = sqlite3.connect("recibos.db")

        # junta os dados do form
        dados = [self.ids.txt_nome.text, self.ids.txt_cpf.text,
                 self.ids.txt_endereco.text, self.ids.txt_bairro.text,
                 self.ids.txt_cidade.text, self.ids.txt_uf.text,
                 self.ids.txt_telefone.text]
        # grava os dados
        banco.cadastrar_recebedor(conexao, dados)
        # fecha a conexão com o banco
        conexao.close()
        self.exibir_popup('Cadastro','Recebedor cadastrado com sucesso!')

        return