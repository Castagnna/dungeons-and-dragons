# Limites
from limite.telaGenerica2 import TelaGenerica

# Controles

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArmaNova(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
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

        janela = sg.Window("Nova arma", default_element_size=(40, 10)).Layout(layout)
        super(TelaArmaNova, self).cria_janela(janela)
