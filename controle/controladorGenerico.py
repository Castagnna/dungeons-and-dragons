from abc import ABC, abstractmethod


class ControladorGenerico(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_tela(self):
        pass

    def finaliza_programa(self):
        confirmacao = input("Tem certeza que quer finalizar o programa? [Y/N]: ")
        if confirmacao in "Yy":
            print("\n---- Programa finalizado -----")
            exit(0)
        else:
            return -1
