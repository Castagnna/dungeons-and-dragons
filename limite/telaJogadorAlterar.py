from limite.telaGenerica import TelaGenerica
import PySimpleGUI as sg

class TelaJogadorAlterar(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__dados_jogador = {'ID': None,
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
                                'player': None,
                                'level': None,
                                'experiencia': None,
                                'proficiencia': None,
                                'CD': None
                                }
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        id = self.__dados_jogador['ID']
        nome = self.__dados_jogador['nome']
        forca = self.__dados_jogador['forca']
        destreza = self.__dados_jogador['destreza']
        constituicao = self.__dados_jogador['constituicao']
        inteligencia = self.__dados_jogador['inteligencia']
        sabedoria = self.__dados_jogador['sabedoria']
        carisma = self.__dados_jogador['carisma']
        imagem = self.__dados_jogador['imagem']
        CA = self.__dados_jogador['CA']
        vida_maxima = self.__dados_jogador['vida_maxima']
        vida_atual = self.__dados_jogador['vida_atual']
        tamanho = self.__dados_jogador['tamanho']
        player = self.__dados_jogador['player']
        level = self.__dados_jogador['level']
        experiencia = self.__dados_jogador['experiencia']
        proficiencia = self.__dados_jogador['proficiencia']
        CD = self.__dados_jogador['CD']

        mensagem = f'Modificar jogador: id: {id}, nome: {nome}'

        layout = [[sg.Text(mensagem, justification='center', size=(30,2))],
                  [sg.Text('Novo nome do jogador:'), sg.InputText(nome, key='NOME')],
                  [sg.Text('Nova forca do jogador:'), sg.InputText(forca, key='FORCA')],
                  [sg.Text('Nova destreza do jogador:'), sg.InputText(destreza, key='DESTREZA')],
                  [sg.Text('Nova constituicao do jogador:'), sg.InputText(constituicao, key='CONSTITUICAO')],
                  [sg.Text('Nova intelgencia do jogador:'), sg.InputText(inteligencia, key='INTELIGENCIA')],
                  [sg.Text('Nova sabedoria do jogador:'), sg.InputText(sabedoria, key='SABEDORIA')],
                  [sg.Text('Novo carisma do jogador:'), sg.InputText(carisma, key='CARISMA')],
                  [sg.Text('Nova imagem do jogador:'), sg.InputText(imagem, key='IMAGEM')],
                  [sg.Text('Nova CA do jogador:'), sg.InputText(CA, key='CA')],
                  [sg.Text('Nova vida maxima do jogador:'), sg.InputText(vida_maxima, key='VIDA_MAXIMA')],
                  [sg.Text('Nova vida atual do jogador:'), sg.InputText(vida_atual, key='VIDA_ATUAL')],
                  [sg.Text('Novo tamanho do jogador:'), sg.InputText(tamanho, key='TAMANHO')],
                  [sg.Text('Novo nome de player:'), sg.InputText(player, key='PLAYER')],
                  [sg.Text('Novo level do jogador'), sg.InputText(level, key='LEVEL')],
                  [sg.Text('Nova experiencia do jogador:'), sg.InputText(experiencia, key='EXPERIENCIA'),
                    [sg.Text('Novo bonus de proficiencia do jogador'), sg.InputText(proficiencia, key='PROFICIENCIA')],
                   [sg.Text('Novo CD dos testes do jogador'), sg.InputText(CD, key='CD')],
                   sg.Submit(), sg.Cancel()]

        ]

        janela = sg.Window('Alterar jogador', default_element_size=(40,10)).Layout(layout)
        super(TelaJogadorAlterar, self).cria_janela(janela)

    def mostra_tela(self, dados: dict):
        self.__dados_jogador = dados
        return super().mostra_tela()