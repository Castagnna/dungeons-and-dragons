from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaJogadorMostraAtributos(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
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
                                'CD': None}

    def init_components(self):
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

        layout = [[sg.Text('ID - ' + str(id))],
                  [sg.Text('Nome - ' + str(nome))],
                  [sg.Text('Forca - ' + str(forca))],
                  [sg.Text('Destreza - ' + str(destreza))],
                  [sg.Text('Constituicao - ' + str(constituicao))],
                  [sg.Text('Intelgencia - ' + str(inteligencia))],
                  [sg.Text('Sabedoria - ' + str(sabedoria))],
                  [sg.Text('Carisma - ' + str(carisma))],
                  [sg.Text('Imagem - ' + str(imagem))],
                  [sg.Text('CA - ' + str(CA))],
                  [sg.Text('Vida maxima - ' + str(vida_maxima))],
                  [sg.Text('Vida atual - ' + str(vida_atual))],
                  [sg.Text('Tamanho - ' + str(tamanho))],
                  [sg.Text('Player - ' + str(player))],
                  [sg.Text('Level - ' + str(level))],
                  [sg.Text('Experiencia - ' + str(experiencia))],
                  [sg.Text('Proficiencia - ' + str(proficiencia))],
                  [sg.Text('CD - ' + str(CD))],
                  [sg.OK('OK', key='CONFIRMA')]
                  ]

        janela = sg.Window('Atributos jogador', default_element_size=(40, 10)).Layout(layout)
        super(TelaJogadorMostraAtributos, self).cria_janela(janela)

    def mostra_atributos_do_personagem(self, jogador: dict):
        self.__dados_jogador = jogador
        return super().mostra_tela()