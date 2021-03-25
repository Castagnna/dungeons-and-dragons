

class Arma:
    def __init__(self, id: int, nome: str, dano: str):
        self.__id = id
        self.__nome = nome
        self.__dano = dano

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def dano(self) -> str:
        return self.__dano

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @dano.setter
    def dano(self, dano: str):
        if isinstance(dano, str):
            self.__dano = dano
