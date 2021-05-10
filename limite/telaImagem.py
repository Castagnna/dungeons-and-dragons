from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaImagem(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [[sg.Text('MENU IMAGEM', size=(20, 1), font=('Helvetica', 25), justification='center')],
                  [sg.Text('Digite o nome da imagem'), sg.InputText('',key='IMAGEM')],
                  [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel('Cancelar', key='CANCELAR')]]

        janela = sg.Window('Menu Imagem', default_element_size=(40, 1)).Layout(layout)
        super(TelaImagem, self).cria_janela(janela)
