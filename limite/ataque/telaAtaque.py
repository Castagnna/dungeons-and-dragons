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
            [sg.Button("Nova ataque", key="NOVO_ATAQUE", size=(20, 2))],
            [sg.Button("Ataques cadastrados", key="LISTA_ATAQUES", size=(20, 2))],
            [sg.Button("Remove ataque", key="REMOVE_ATAQUE", size=(20, 2))],
            [sg.Button("Alterar ataque", key="ARTERA_ATAQUE", size=(20, 2))],
            [sg.Button("Cria ataque teste", key="ATAQUE_TESTE", size=(20, 2))],
            [sg.Cancel("Voltar", key="VOLTAR", size=(20, 2))],
        ],

        janela = sg.Window(
            title="Menu ataques",
            size=(300, 375),
            resizable=True,
            element_justification="center",
            ).Layout(layout)
            
        super(TelaAtaque, self).cria_janela(janela)
