from abc import ABC, abstractmethod


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador, titulo_da_tela: str,
                 opcoes: tuple = None):
        self.__controlador = controlador
        self.__titulo_da_tela = titulo_da_tela
        self.__id_opcoes = [id for id, _ in opcoes] + [0]
        self.__opcoes = [opcao for _, opcao in opcoes] + ["Encerrar programa"]

    @property
    def controlador(self):
        return self.__controlador

    def mostra_opcoes(self) -> int:
        self.cria_menu_opcoes()
        opcao = self.le_numero_inteiro("\n>>> Escolha uma opção: ")
        if opcao == 0:
            confirma = input("Tem certeza que quer finalizar o programa? [Y/N]: ")
            if confirma in "Yy":
                print("\n---- Programa finalizado -----")
            else:
                return -1
        return opcao

    def cria_menu_opcoes(self):
        print("------ {} ------".format(self.__titulo_da_tela))
        for id, opcao in zip(self.__id_opcoes, self.__opcoes):
            print("{} - {}".format(id, opcao))

    def le_numero_inteiro(self, mensagem: str) -> int:
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiro not in self.__id_opcoes:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto, por favor digite um inteiro valido!")
                print("Valores validos: ", self.__id_opcoes)

    @staticmethod
    def tela_confirma(mensagem: str) -> bool:
        confirma = input(mensagem + " [Y/N] ")
        return confirma in "Yy"

    def pega_dado(self, mensagem: str, tipo: str):
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
            except ValueError:
                print("O dado deve ser do tipo {}, tente novamente.".format(tipo))
                pass
            else:
                mensagem = "Confirma o valor >> {} << ?".format(dado)
                if self.tela_confirma(mensagem):
                    return dado
