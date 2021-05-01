# Entidades
from entidade.arma import Arma

# Limites
from limite.telaGenerica import GeneralScreen

# Controles

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArmaNova(GeneralScreen):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Nova arma', background_color='#d3dfda', justification='center', size=(10, 2))],
            [sg.Text("Nome da arma:"), sg.InputText("", key="NOME")],
            [sg.Text("Quantidade de dados:"), sg.Slider(range=(1, 10), orientation='h', size=(10, 20), default_value=1, key="DADOS")],
            [sg.Text("Numero de faces:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=1, key="FACES")],
            [sg.Submit("Confirmar", key="CONFIRMAR"), sg.Cancel("Cancelar", key="CANCELAR")],
        ],

        self.__janela = sg.Window("Nova arma", default_element_size=(40, 10)).Layout(layout)

    def mostra_tela(self):
        return self.__janela.Read()

    def fecha_tela(self):
        self.__janela.Close()