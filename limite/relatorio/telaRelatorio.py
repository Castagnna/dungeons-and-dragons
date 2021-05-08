# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaRelatorio(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button("Relatório de combates", key="COMBATE")],
            [sg.Cancel("Voltar", key="VOLTAR")],
        ],

        janela = sg.Window("Relatorios", default_element_size=(40, 50)).Layout(layout)
        super(TelaRelatorio, self).cria_janela(janela)
