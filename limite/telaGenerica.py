from abc import ABC, abstractmethod


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador) -> object:
        self.__controlador = controlador
        self.__dicio_letras = {"A": 100, "B": 200, "C": 300, "D": 400, "E": 500,
                               "F": 600, "G": 700, "H": 800, "I": 900, "J": 1000,
                               "K": 1100, "L": 1200, "M": 1300, "N": 1400, "O": 1500,
                               "P": 1600, "Q": 1700, "R": 1800, "S": 1900,
                               "T": 2000, "U": 2100, "V": 2200, "W": 2300,
                               "X": 2400, "Y": 2500, "Z": 2500}
        self.__dicio_numeros = {"1": 100, "2": 200, "3": 300, "4": 400, "5": 500, "6": 600, "7": 700, "8": 800,
                                "9": 900}

    @property
    def controlador(self):
        return self.__controlador

    @controlador.setter
    def controlador(self, controlador):
        self.__controlador = controlador

    @abstractmethod
    def mostra_opcoes(self) -> int:
        pass

    @staticmethod
    def cria_menu_opcoes(titulo_da_tela: str, opcoes: tuple = None):
        print("------ {} ------".format(titulo_da_tela.upper()))
        for codigo, opcao in opcoes:
            print("{:02d} - {}".format(codigo, opcao))

    @staticmethod
    def tela_confirma(mensagem: str) -> bool:
        confirma = input(mensagem + " [Y/N]: ").strip()
        return len(confirma) == 1 and confirma in "Yy"

    def protege_finalizar(self, opcao: int) -> int:
        if opcao == 99:
            mensagem = "Tem certeza que quer finalizar o programa?"
            if self.tela_confirma(mensagem):
                print("\n---- Programa finalizado -----")
                return opcao
            else:
                return -1
        return opcao

    def pega_dado(self,
                  mensagem: str,
                  tipo: str,
                  valores_validos: list = None,
                  confirmar: bool = True):

        tipos = {
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
        }

        while True:
            dado = input(mensagem)
            try:
                dado = tipos[tipo](dado)
                if valores_validos and dado not in valores_validos:
                    raise ValueError
            except ValueError:
                print("O valor deve ser tipo {}".format(tipo), end="")
                if valores_validos:
                    print(" dentre os valores {}".format(valores_validos), end="")
                print(", tente novamente.")
                pass
            else:
                if not confirmar:
                    return dado
                else:
                    msg_confirmacao = "Confirma o valor >> {} << ?".format(dado)
                    if self.tela_confirma(msg_confirmacao):
                        return dado

    @staticmethod
    def monstra_mensagem(mensagem: str):
        print("\n" + mensagem + "\n")

    def executado_com_sucesso(self):
        self.monstra_mensagem("Operacao executada com sucesso")

    def pega_id(self, valores_validos: list) -> int:
        return self.pega_dado("escolha por Id: ", "int", valores_validos, False)
