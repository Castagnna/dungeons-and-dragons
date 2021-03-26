# import pygame
import random

class Arma:
    def __init__(self, nome: str, quantidade_dado: int, numero_faces: int):
        self.__nome = nome
        self.__quantidade_dado = quantidade_dado
        self.__numero_faces = numero_faces

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

    def dano(self):
        contador = 0
        for i in range(self.__quantidade_dado):
            contador += random.randint(1, self.__numero_faces)
        return contador