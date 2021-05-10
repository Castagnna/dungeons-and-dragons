from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaPersonagemTamanho(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [[sg.Text('TAMANHO', justification='center', size=(30, 2))],
                  [sg.Text('Tamanho:'), sg.InputText('', key='TAMANHO')],
                  [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel('Cancelar', key='CANCELAR')]]

        janela = sg.Window('Tamanho do personagem', default_element_size=(40, 1)).Layout(layout)
        super(TelaPersonagemTamanho, self).cria_janela(janela)