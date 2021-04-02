import pygame

class Magia:
    def __init__(self, id: int, nome: str, quantidade_dado: int, numero_faces: int, circulo: int, teste: list):
        self.__id = id
        self.__nome = nome
        self.__quantidade_dado = quantidade_dado
        self.__numero_faces = numero_faces
        self.__circulo = circulo
        self.__teste = teste

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def quantidade_dado(self):
        return self.__quantidade_dado

    @quantidade_dado.setter
    def quantidade_dado(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade_dado = quantidade

    @property
    def numero_faces(self):
        return self.__numero_faces

    @numero_faces.setter
    def numero_faces(self, dado: int):
        if isinstance(dado, int):
            self.__numero_faces = dado

    @property
    def circulo(self):
        return self.__circulo

    @circulo.setter
    def circulo(self, circulo: int):
        if isinstance(circulo, int):
            self.__circulo = circulo

    @property
    def teste(self):
        return self.__teste

    @teste.setter
    def teste(self, teste):
        if isinstance(teste, str):
            self.__teste = teste
