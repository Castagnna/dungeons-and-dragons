from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg


class TelaMagia(TelaGenerica):
    def __init__(self, controlador):
        super(TelaMagia, self).__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Button('Nova magia', key='NOVA_MAGIA')],
            [sg.Button('Alterar magia', key='ALTERA_MAGIA')],
            [sg.Button('Voltar', key='VOLTAR')]
        ]

        janela = sg.Window('Menu Magia', default_element_size=(40, 50)).Layout(layout)
        super(TelaMagia, self).cria_janela(janela)