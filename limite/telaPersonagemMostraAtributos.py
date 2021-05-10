from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaPersonagemMostraAtributos(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.__atributos = None
        self.init_components()

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        layout = []

        for i in range(len(self.__atributos)):
            layout.append([sg.Text(str(self.__atributos[i]))])
        layout.append(sg.OK('OK'))

        janela = sg.Window('Armas do Jogador', default_element_size=(30, 10)).Layout(layout)
        super(TelaPersonagemMostraAtributos, self).cria_janela(janela)

    def mostra_atributos_do_personagem(self, atributos: dict):
        self.__atributos = atributos
        self.init_components()
        self.__janela.Read()