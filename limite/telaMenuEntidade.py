from limite.telaGenerica import TelaGenerica
from abc import abstractmethod
import PySimpleGUI as sg

class MenuEntidade(TelaGenerica):
    @abstractmethod
    def __init__(self, controlador):
        super(MenuEntidade, self).__init__(controlador)
        self.__menu = ''
        self.__opcoes = dict()
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = []
        layout.append([sg.Text(self.__menu, size=(20,1), font=('Helvetica',25), justification='center')])
        for i in range(len(self.__opcoes)):
            layout.append([sg.Button(self.__opcoes[i+1], key=i+1)])
        layout.append([sg.Button('Voltar', key=88)])
        layout.append([sg.Button('Finaliza programa', key=99)])

        self.__janela = sg.Window('Trabalho DSO', default_element_size=(40, 1)).Layout(layout)

    def mostra_opcoes(self, menu: str, opcoes: dict):
        self.__menu = menu
        self.__opcoes = opcoes
        self.init_components()
        return self.__janela.Read()