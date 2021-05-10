# Limites
from limite.telaGenerica import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaRelatorio(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button("Relatório de combates", key="COMBATE", size=(20, 2))],
            [sg.Cancel("Voltar", key="VOLTAR", size=(20, 2))],
        ],

        janela = sg.Window(
            title="Relatorios",
            size=(300, 375),
            resizable=True,
            element_justification="center",
            ).Layout(layout)

        super(TelaRelatorio, self).cria_janela(janela)
