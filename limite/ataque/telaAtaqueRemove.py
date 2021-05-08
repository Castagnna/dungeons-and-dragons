# Limites
from limite.telaGenerica2 import TelaGenerica

# Controles

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaAtaqueRemove(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text("Id da ataque para remover:"), sg.InputText("", key="ID")],
            [sg.Submit("Confirmar", key="CONFIRMAR"), sg.Cancel("Cancelar", key="CANCELAR")],
        ],

        janela = sg.Window("Remover Ataque", default_element_size=(30, 10)).Layout(layout)
        super(TelaAtaqueRemove, self).cria_janela(janela)
