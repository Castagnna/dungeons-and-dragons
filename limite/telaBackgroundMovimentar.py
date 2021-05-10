from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaBackgroundMovimentar(TelaGenerica):
    def __init__(self, controlador):
        super(TelaBackgroundMovimentar, self).__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Text('MENU MOVIMENTAR MAPA', size=(20, 1), font=('Helvetica', 25), justification='center')],
                  [sg.Button('Cima', key='1')],
                  [sg.Button('Esquerda', key='2')],
                  [sg.Button('Direita', key='3')],
                  [sg.Button('Baixo', key='4')],
                  [sg.Button('Voltar', key=88)],
                  [sg.Button('Finalizar Programa', key=99)]]

        janela = sg.Window('Trabalho DSO', default_element_size=(40, 1)).Layout(layout)
        super(TelaBackgroundMovimentar, self).cria_janela(janela)