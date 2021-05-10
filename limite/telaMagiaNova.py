from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg


class TelaMagiaNova(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                  [sg.Text('Nome da magia:'), sg.InputText('', key='NOME')],
                  [sg.Text('Quantidade de dados:'), sg.Slider(range=(1, 10), orientation='h', size=(10,20), default_value=1, key='DADOS')],
                  [sg.Text('Numero de faces:'), sg.Slider(range=(1,20), orientation='h', size=(10,20), default_value=1, key='FACES')],
                  [sg.Text('Circulo de magia:'), sg.Slider(range=(0,9), orientation='h', size=(10,20), default_value=0, key='CIRCULO')],
                  [sg.Text('Alvo realiza teste:'), sg.InputText('Nenhum', key='TESTE')],
                  [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel(('Cancelar'))]
                  ]

        janela = sg.Window('Nova magia', default_element_size=(40,10)).Layout(layout)
        super(TelaMagiaNova, self).cria_janela(janela)