# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaPrincipal(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Button("Menu Jogador", key="JOGADOR")],
            [sg.Button("Menu Monstro", key="MONSTRO")],
            [sg.Button("Menu Arma", key="ARMA")],
            [sg.Button("Menu Ataque Monstro", key="ATAQUE_MONSTRO")],
            [sg.Button("Menu Background", key="BACKGROUND")],
            [sg.Button("Menu Relatorio", key="RELATORIO")],
            [sg.Button("Finaliza Programa", key="FINALIZAR")],
        ],

        janela = sg.Window(title="Dungeons & Dragons").Layout(layout)
        super(TelaPrincipal, self).cria_janela(janela)
