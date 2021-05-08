# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button("Nova arma", key="NOVA_ARMA")],
            [sg.Button("Armas cadastradas", key="LISTA_ARMAS")],
            [sg.Button("Remove arma", key="REMOVE_ARMA")],
            [sg.Button("Alterar arma", key="ARTERA_ARMA")],
            [sg.Button("Cria arma teste", key="ARMA_TESTE")],
            [sg.Cancel("Voltar", key="VOLTAR")],
        ],

        janela = sg.Window("Menu armas", default_element_size=(40, 50)).Layout(layout)
        super(TelaArma, self).cria_janela(janela)
