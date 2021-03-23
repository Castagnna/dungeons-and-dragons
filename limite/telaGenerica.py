from abc import ABC, abstractmethod


class TelaGenerica(ABC):
    @abstractmethod
    def __init__(self, controlador, titulo_da_tela: str,
                 opcoes: tuple = None):
        self.__controlador = controlador
        self.__titulo_da_tela = titulo_da_tela
        self.__id_opcoes = [id for id, _ in opcoes] + [0]
        self.__opcoes = [opcao for _, opcao in opcoes] + ["Encerrar programa"]

    def mostra_opcoes(self):
        self.cria_menu_opcoes()
        return self.le_numero_inteiro(">>> Escolha uma opção: ")

    def cria_menu_opcoes(self):
        print("------ {} ------".format(self.__titulo_da_tela))
        for id, opcao in zip(self.__id_opcoes, self.__opcoes):
            print("{} - {}".format(id, opcao))

    def le_numero_inteiro(self, mensagem: str):
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
