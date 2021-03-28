from abc import ABC, abstractmethod


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador, titulo_da_tela: str,
                 opcoes: tuple = None):
        self.__controlador = controlador
        self.__titulo_da_tela = titulo_da_tela
        self.__id_opcoes = [id for id, _ in opcoes] + [99]
        self.__opcoes = [opcao for _, opcao in opcoes] + ["Encerrar programa"]

    @property
    def controlador(self):
        return self.__controlador

    def mostra_opcoes(self) -> int:
        self.cria_menu_opcoes()
        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=self.__id_opcoes,
            confirmar=False
        )
        if opcao == 99:
            mensagem = "Tem certeza que quer finalizar o programa?"
            if self.tela_confirma(mensagem):
                print("\n---- Programa finalizado -----")
            else:
                return -1
        return opcao

    def cria_menu_opcoes(self):
        print("------ {} ------".format(self.__titulo_da_tela))
        for id, opcao in zip(self.__id_opcoes, self.__opcoes):
            print("{} - {}".format(id, opcao))

    @staticmethod
    def tela_confirma(mensagem: str) -> bool:
        confirma = input(mensagem + " [Y/N]: ")
        return confirma in "Yy"

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
                print("O dado deve ser do tipo {}".format(tipo), end="")
                if valores_validos:
                    print(" e deve ser {}".format(valores_validos), end="")
                print(", tente novamente.")
                pass
            else:
                if not confirmar:
                    return dado
                else:
                    msg_confirmacao = "Confirma o valor >> {} << ?".format(dado)
                    if self.tela_confirma(msg_confirmacao):
                        return dado
