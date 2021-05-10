from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg


class TelaMonstroNovo(TelaGenerica):
    def __init__(self, controlador):
        super(TelaMonstroNovo, self).__init__(controlador)
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                  [sg.Text('Digite o nome do monstro'), sg.InputText('', key='NOME')],
                  [sg.Text('Digite a forca do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='FORCA')],
                  [sg.Text('Digite a destreza do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='DESTREZA')],
                  [sg.Text('Digite a constituicao do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CONSTITUICAO')],
                  [sg.Text('Digite a inteligencia do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='INTELIGENCIA')],
                  [sg.Text('Digite a sabedoria do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='SABEDORIA')],
                  [sg.Text('Digite o carisma do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CARISMA')],
                  [sg.Text('Digite o nome da imagem'), sg.InputText('', key='IMAGEM')],
                  [sg.Text('Digite a CA do monstro'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CA')],
                  [sg.Text('Digite a vida maxima do monstro'), sg.Slider(range=(1, 1000), orientation='h', size=(10, 20), default_value=1, key='VIDA_MAXIMA')],
                  [sg.Text('Digite a vida atual do monstro'), sg.Slider(range=(1, 1000), orientation='h', size=(10, 20), default_value=1, key='VIDA_ATUAL')],
                  [sg.Text('Digite o tamanho do monstro'), sg.InputText('', key='TAMANHO')],
                  [sg.Text('Digite o tipo do monstro'), sg.InputText('', key='TIPO')],
                  [sg.Text('Digite a experiencia do monstro'), sg.InputText('', key='EXPERIENCIA')],
                  [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel('Cancelar', key='CANCELAR')]
        ]

        janela = sg.Window('Novo monstro', default_element_size=(40, 1)).Layout(layout)
        super(TelaMonstroNovo, self).cria_janela(janela)
