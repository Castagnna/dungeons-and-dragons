from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaJogadorMostraArmas(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.__armas = []
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = []

        for i in self.__armas:
            layout.append([sg.Text(str(i[0]) + ' - ' + i[1])])
        layout.append(sg.OK('OK', key='CONFIRMAR'))

        janela = sg.Window('Armas do Jogador', default_element_size=(30, 10)).Layout(layout)
        super(TelaJogadorMostraArmas, self).cria_janela(janela)

    def mostra_armas_do_jogador(self, armas: list):
        self.__armas = armas
        self.init_components()
        self.__janela.Read()