import PySimpleGUI as sg

class TelaImagemException():
    def __init__(self):
        self.__janela = None
        self.init_components()

    def init_components(self):
        layout = [[sg.Text('ERRO', size=(30, 1), font=('Helvetica', 25), justification='center')],
                  [sg.Text('Imagem nao encontrada')],
                  [sg.OK('OK', key='CONFIRMAR')]]

        self.__janela = sg.Window('Trabalho DSO', default_element_size=(40, 1)).Layout(layout)

    def fecha_tela(self):
        self.__janela.Close()

    def mostra_erro(self):
        self.init_components()
        return self.__janela.Read()
