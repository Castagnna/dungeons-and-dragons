from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaBackground(TelaGenerica):
    def __init__(self, controlador):
        super(TelaBackground, self).__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Button('Criar/Alterar Background', key='INSERI_MAPA')],
            [sg.Button('Movimentar Mapa', key='MOVIMENTA_MAPA')],
            [sg.Button('Voltar', key='VOLTAR')]
        ]

        janela = sg.Window('Menu Jogador', default_element_size=(40,50)).Layout(layout)
        super(TelaBackground, self).cria_janela(janela)