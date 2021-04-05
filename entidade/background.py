import pygame


class Background():
    def __init__(self, imagem: pygame.image.load, posicao: list):
        self.__imagem = imagem
        self.__posicao = posicao

    @property
    def imagem(self):
        return self.__imagem

    @property
    def posicao(self):
        return self.__posicao[:2]

    def movimentar(self, lista: list):
        self.__posicao[0] -= lista[0]
        self.__posicao[1] -= lista[1]
