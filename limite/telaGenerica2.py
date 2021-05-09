from controle.controladorGenerico import ControladorGenerico

# Utils
from PySimpleGUI import PySimpleGUI as sg
from abc import ABC, abstractmethod


class TelaGenerica(ABC):

    @abstractmethod
    def __init__(self, controlador: ControladorGenerico):
        self.__controlador = controlador
        self.__janela = None

    """
    getters
    """

    @property
    def controlador(self) -> ControladorGenerico:
        return self.__controlador

    @property
    def janela(self):
        return self.__janela

    """
    setters
    """

    @controlador.setter
    def controlador(self, controlador: ControladorGenerico):
        self.__controlador = controlador

    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    """
    methods
    """

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
    def popup_sucesso(titulo: str="Sucesso", mensagem: str=None):
        if not mensagem:
            mensagem = "Operacao realizada com sucesso"
        sg.Popup(titulo, mensagem)

    @staticmethod
    def popup_falha(titulo: str="Erro", mensagem: str=None):
        if not mensagem:
            mensagem = "Nao foi possivel concluir a operacao"
        sg.Popup(titulo, mensagem)

    @staticmethod
    def yes_or_no(titulo: str="Prossegir?"):
        return sg.PopupYesNo(title=titulo)
