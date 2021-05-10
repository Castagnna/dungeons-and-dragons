# Limites
from limite.telaGenerica import TelaGenerica

# Controles

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArmaRemove(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Id da arma para remover:"), sg.InputText("", key="ID")],
            [sg.Submit("Confirmar", key="CONFIRMAR"), sg.Cancel("Cancelar", key="CANCELAR")],
        ],

        janela = sg.Window("Remover Arma", default_element_size=(30, 10)).Layout(layout)
        super(TelaArmaRemove, self).cria_janela(janela)
