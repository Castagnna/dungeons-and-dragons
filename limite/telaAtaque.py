# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaAtaque(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button("Nova ataque", key="NOVO_ATAQUE")],
            [sg.Button("Ataques cadastradas", key="LISTA_ATAQUES")],
            [sg.Button("Remove ataque", key="REMOVE_ATAQUE")],
            [sg.Button("Alterar ataque", key="ARTERA_ATAQUE")],
            [sg.Button("Cria ataque teste", key="ATAQUE_TESTE")],
            [sg.Cancel("Voltar", key="VOLTAR")],
        ],

        janela = sg.Window("Menu ataques", default_element_size=(40, 50)).Layout(layout)
        super(TelaAtaque, self).cria_janela(janela)
