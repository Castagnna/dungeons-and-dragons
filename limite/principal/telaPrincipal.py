# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaPrincipal(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        # sg.ChangeLookAndFeel("Reddit")

        layout = [
            [sg.Button("Menu Jogador", key="JOGADOR", size=(20, 2))],
            [sg.Button("Menu Monstro", key="MONSTRO", size=(20, 2))],
            [sg.Button("Menu Arma", key="ARMA", size=(20, 2))],
            [sg.Button("Menu Ataque Monstro", key="ATAQUE_MONSTRO", size=(20, 2))],
            [sg.Button("Menu Background", key="BACKGROUND", size=(20, 2))],
            [sg.Button("Menu Relatorio", key="RELATORIO", size=(20, 2))],
            [sg.Button("Finaliza Programa", key="FINALIZAR", size=(20, 2))],
        ],

        janela = sg.Window(
            title="Dungeons & Dragons",
            size=(300, 375),
            resizable=True,
            element_justification="center",
            ).Layout(layout)
        super(TelaPrincipal, self).cria_janela(janela)
