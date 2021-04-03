from abc import ABC, abstractmethod


class ControladorGenerico(ABC):
    @abstractmethod
    def __init__(self, tela):
        self.__tela = tela
        self.__mostra_tela = True

    @abstractmethod
    def mostra_tela(self, funcoes: dict):
        self.__mostra_tela = True

        funcoes[-1] = self.mesma_tela
        funcoes[88] = self.fecha_tela
        funcoes[99] = self.finaliza_programa

        while self.__mostra_tela:
            opcao_selecionada = self.__tela.mostra_opcoes()
            funcao_selecionada = funcoes[opcao_selecionada]
            funcao_selecionada()

    def fecha_tela(self):
        self.__mostra_tela = False

    def mesma_tela(self):
        pass

    @staticmethod
    def finaliza_programa():
        exit(0)

    @property
    def tela(self):
        return self.__tela
