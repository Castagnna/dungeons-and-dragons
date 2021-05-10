from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaMonstroMostraAtributos(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
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
                                'experiencia': None}

    def init_components(self):
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
                  [sg.Text('Tipo - ' + str(tipo))],
                  [sg.Text('Experiencia - ' + str(experiencia))],
                  [sg.OK('OK', key='CONFIRMA')]
                  ]

        janela = sg.Window('Atributos monstro', default_element_size=(40, 10)).Layout(layout)
        super(TelaMonstroMostraAtributos, self).cria_janela(janela)

    def mostra_atributos_do_personagem(self, monstro: dict):
        self.__dados_monstro = monstro
        return super().mostra_tela()