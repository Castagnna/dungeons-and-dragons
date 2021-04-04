import pygame


class Background():
    def __init__(self, imagem: pygame.image.load, posicao: list):
        self.__imagem = imagem
        self.__posicao = posicao

    def posicao(self):
        self.__posicao = self.__imagem.get_rect()

    def movimentar(self, lista: list):
        self.__posicao[0] -= lista[0]
        self.__posicao[1] -= lista[1]
