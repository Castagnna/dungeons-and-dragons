# Limites
from limite.telaGenerica import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArma(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button("Nova arma", key="NOVA_ARMA", size=(20, 2))],
            [sg.Button("Armas cadastradas", key="LISTA_ARMAS", size=(20, 2))],
            [sg.Button("Remove arma", key="REMOVE_ARMA", size=(20, 2))],
            [sg.Button("Alterar arma", key="ARTERA_ARMA", size=(20, 2))],
            [sg.Button("Cria arma teste", key="ARMA_TESTE", size=(20, 2))],
            [sg.Cancel("Voltar", key="VOLTAR", size=(20, 2))],
        ],

        janela = sg.Window(
            title="Menu armas",
            size=(300, 375),
            resizable=True,
            element_justification="center",
            ).Layout(layout)

        super(TelaArma, self).cria_janela(janela)
