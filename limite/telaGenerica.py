from abc import ABC, abstractmethod


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador, titulo_da_tela: str,
                 id_opcoes: tuple = None, opcoes: tuple = None):
        self.__controlador = controlador
        self.__titulo_da_tela = titulo_da_tela
        self.__id_opcoes = id_opcoes
        self.__opcoes = opcoes

    def mostra_opcoes(self):
        self.cria_menu_opcoes()
        return self.le_numero_inteiro(">>> Escolha uma opção: ")

    def cria_menu_opcoes(self):
        print("------ {} ------".format(self.__titulo_da_tela))
        for id, opcao in zip(self.__id_opcoes, self.__opcoes):
            print("{} - {}".format(id, opcao))
        print("0 - Encerrar programa")

    def le_numero_inteiro(self, mensagem: str):
        valores_validos = list(self.__id_opcoes)
        valores_validos.append(0)
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiro not in valores_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto, por favor digite um inteiro valido.")
                print("Valores validos: ", valores_validos)
