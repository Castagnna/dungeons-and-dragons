from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaPersonagemAtaque(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.__ataques = None
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = []

        for i in self.__ataques:
            layout.append([sg.Button(i[1], key=i[0])])
        layout.append(sg.Cancel('Voltar', key='VOLTAR'))

        janela = sg.Window('Armas do Jogador', default_element_size=(30, 10)).Layout(layout)
        super(TelaPersonagemAtaque, self).cria_janela(janela)

    def mostra_ataques(self, ataques):
        self.__ataques = ataques
        self.init_components()
        self.__janela.Read()