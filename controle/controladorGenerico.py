from abc import ABC, abstractmethod


class ControladorGenerico(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_tela(self):
        pass

    def finaliza_programa(self):
        exit(0)
