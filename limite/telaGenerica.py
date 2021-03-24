from abc import ABC, abstractmethod


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador, titulo_da_tela: str,
                 opcoes: tuple = None):
        self.__controlador = controlador
        self.__titulo_da_tela = titulo_da_tela
        self.__id_opcoes = [id for id, _ in opcoes] + [0]
        self.__opcoes = [opcao for _, opcao in opcoes] + ["Encerrar programa"]

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
    def pega_dado(mensagem: str, tipo: str):
        tipos = {
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
        }
        continua = True

        while continua:
            dado = input(mensagem)
            try:
                dado = tipos[tipo](dado)
            except ValueError:
                print("O dado e o seu tipo não conferem, tente novamente.")
                pass
            else:
                confirma = input("Confirma o valor >> {} << ? [Y/N] ".format(dado))
                if confirma in "Yy":
                    continua = False
