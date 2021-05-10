from abc import ABC, abstractmethod
import PySimpleGUI as sg


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador) -> object:
        self.__janela = None
        self.__controlador = controlador

    @property
    def controlador(self):
        return self.__controlador

    @controlador.setter
    def controlador(self, controlador):
        self.__controlador = controlador

    @property
    def janela(self):
        return self.__janela

    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    def cria_janela(self, janela):
        self.__janela = janela

    @abstractmethod
    def init_components(self):
        pass

    def mostra_tela(self):
        self.init_components()
        return self.__janela.Read()

    def fecha_tela(self):
        self.__janela.Close()

    @staticmethod
    def popup_sucesso(titulo: str='Sucesso', mensagem: str=None):
        if not mensagem:
            mensagem = 'Operacao realizada com sucesso'
        sg.Popup(titulo, mensagem)

    @staticmethod
    def popup_falha(titulo: str='Erro', mensagem: str=None):
        if not mensagem:
            mensagem = 'Nao foi possivel concluir operacao'
        sg.Popup(titulo, mensagem)

    @staticmethod
    def yes_or_no(titulo: str = "Prossegir?"):
        return sg.PopupYesNo(title=titulo)