from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaMonstroAlterar(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__dados_monstro = {'ID': None,
                                'nome': None,
                                'forca': None,
                                'destreza': None,
                                'constituicao': None,
                                'inteligencia': None,
                                'sabedoria': None,
                                'carisma': None,
                                'imagem': None,
                                'CA': None,
                                'vida_maxima': None,
                                'vida_atual': None,
                                'tamanho': None,
                                'tipo': None,
                                'experiencia': None
        }

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        id = self.__dados_monstro['ID']
        nome = self.__dados_monstro['nome']
        forca = self.__dados_monstro['forca']
        destreza = self.__dados_monstro['destreza']
        constituicao = self.__dados_monstro['constituicao']
        inteligencia = self.__dados_monstro['inteligencia']
        sabedoria = self.__dados_monstro['sabedoria']
        carisma = self.__dados_monstro['carisma']
        imagem = self.__dados_monstro['imagem']
        CA = self.__dados_monstro['CA']
        vida_maxima = self.__dados_monstro['vida_maxima']
        vida_atual = self.__dados_monstro['vida_atual']
        tamanho = self.__dados_monstro['tamanho']
        tipo = self.__dados_monstro['tipo']
        experiencia = self.__dados_monstro['experiencia']

        mensagem = f'Modificar monstro: id: {id}, nome: {nome}'

        layout = [[sg.Text(mensagem, justification='center', size=(30,2))],
                  [sg.Text('Novo nome do monstro:'), sg.InputText(nome, key='nome')],
                  [sg.Text('Nova forca do monstro:'), sg.InputText(forca, key='forca')],
                  [sg.Text('Nova destreza do monstro:'), sg.InputText(destreza, key='destreza')],
                  [sg.Text('Nova constituicao do monstro:'), sg.InputText(constituicao, key='constituicao')],
                  [sg.Text('Nova intelgencia do monstro:'), sg.InputText(inteligencia, key='inteligencia')],
                  [sg.Text('Nova sabedoria do monstro:'), sg.InputText(sabedoria, key='sabedoria')],
                  [sg.Text('Novo carisma do monstro:'), sg.InputText(carisma, key='carisma')],
                  [sg.Text('Nova imagem do monstro:'), sg.InputText(imagem, key='imagem')],
                  [sg.Text('Nova CA do monstro:'), sg.InputText(CA, key='CA')],
                  [sg.Text('Nova vida maxima do monstro:'), sg.InputText(vida_maxima, key='vida_maxima')],
                  [sg.Text('Nova vida atual do monstro:'), sg.InputText(vida_atual, key='vida_atual')],
                  [sg.Text('Novo tamanho do monstro:'), sg.InputText(tamanho, key='tamanho')],
                  [sg.Text('Novo tipo de monstro:'), sg.InputText(tipo, key='player')],
                  [sg.Text('Nova experiencia do monstro:'), sg.InputText(experiencia, key='experiencia')],
                  [sg.Submit(), sg.Cancel()]
                  ]

        janela = sg.Window('Alterar jogador', default_element_size=(40, 10)).Layout(layout)
        super(TelaMonstroAlterar, self).cria_janela(janela)

    def mostra_tela(self, dados: dict):
        self.__dados_monstro = dados
        return super().mostra_tela()