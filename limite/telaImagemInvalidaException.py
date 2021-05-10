import PySimpleGUI as sg

class TelaImagemInvalidaException:
    def __init__(self):
        self.__janela = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [[sg.Text('IMAGEM', justification='center', size=(30, 2))],
                  [sg.Text('Imagem:'), sg.InputText('', key='IMAGEM')]]

        janela = sg.Window('Trabalho DSO', default_element_size=(40, 1)).Layout(layout)
        self.__janela = janela

        return self.__janela.Read()