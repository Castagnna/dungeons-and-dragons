from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaPersonagemMovimentar(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None


    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Digite a letra que corresponde a posicao:'), sg.InputText('',key='X')],
            [sg.Text('Digite o numero que corresponde a posicao:'), sg.InputText('', key='Y')],
            [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel('Cancelar', key='CANCELAR')]
        ]

        janela = sg.Window('Monvimentar Personagem', default_element_size=(30, 10)).Layout(layout)
        super(TelaPersonagemMovimentar, self).cria_janela(janela)