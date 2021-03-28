from abc import ABC, abstractmethod


class ControladorGenerico(ABC):
    @abstractmethod
    def __init__(self, tela):
        self.__tela = tela

    @abstractmethod
    def mostra_tela(self, funcoes: dict):
        
        funcoes[-1] = self.mostra_tela
        funcoes[99] = self.finaliza_programa

        while True:
            opcao_selecionada = self.__tela.mostra_opcoes()
            funcao_selecionada = funcoes[opcao_selecionada]
            funcao_selecionada()

    @staticmethod
    def finaliza_programa():
        exit(0)

    @property
    def tela(self):
        return self.__tela
