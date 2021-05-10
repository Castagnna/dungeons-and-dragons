from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg


class TelaJogadorNovo(TelaGenerica):
    def __init__(self, controlador):
        super(TelaJogadorNovo, self).__init__(controlador)
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
                  [sg.Text('Digite o nome do jogador'), sg.InputText('', key='NOME')],
                  [sg.Text('Digite a forca do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='FORCA')],
                  [sg.Text('Digite a destreza do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='DESTREZA')],
                  [sg.Text('Digite a constituicao do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CONSTITUICAO')],
                  [sg.Text('Digite a inteligencia do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='INTELIGENCIA')],
                  [sg.Text('Digite a sabedoria do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='SABEDORIA')],
                  [sg.Text('Digite o carisma do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CARISMA')],
                  [sg.Text('Digite o nome da imagem'), sg.InputText('', key='IMAGEM')],
                  [sg.Text('Digite a CA do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CA')],
                  [sg.Text('Digite a vida maxima do jogador'), sg.Slider(range=(1,150), orientation='h', size=(10, 20), default_value=1, key='VIDA_MAXIMA')],
                  [sg.Text('Digite a vida atual do jogador'), sg.Slider(range=(1,150), orientation='h', size=(10, 20), default_value=1, key='VIDA_ATUAL')],
                  [sg.Text('Digite o tamanho do jogador'), sg.InputText('', key='TAMANHO')],
                  [sg.Text('Digite o nome do player'), sg.InputText('', key='PLAYER')],
                  [sg.Text('Digite o level do jogador'), sg.Slider(range=(1,19), orientation='h', size=(10, 20), default_value=1, key='LEVEL')],
                  [sg.Text('Digite a experiencia do jogador'), sg.Slider(range=(1,50000), orientation='h', size=(100, 20), default_value=1, key='EXPERIENCIA')],
                  [sg.Text('Digite o bonus de proficiencia do jogador'), sg.Slider(range=(1,6), orientation='h', size=(10, 20), default_value=1, key='PROFICIENCIA')],
                  [sg.Text('Digite o CD dos testes do jogador'), sg.Slider(range=(1,30), orientation='h', size=(10, 20), default_value=1, key='CD')],
                  [sg.Submit('Confirmar', key='CONFIRMAR'), sg.Cancel()]
        ]

        janela = sg.Window('Novo jogador', default_element_size=(40, 1)).Layout(layout)
        super(TelaJogadorNovo, self).cria_janela(janela)
