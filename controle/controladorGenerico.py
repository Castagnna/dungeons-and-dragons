from abc import ABC, abstractmethod


class ControladorGenerico(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def iniciar(self):
        pass

    def finaliza_programa(self):
        print("----- Programa finalizado -----")
        exit(0)
