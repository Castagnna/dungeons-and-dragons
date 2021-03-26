from entidade.personagem import Personagem
import pygame


class Monstro(Personagem):
    def __init__(self, codigo: int, nome: str, forca: int, destreza: int, constituicao: int,
                 inteligencia: int, sabedoria: int, carisma: int, imagem: pygame.image.load,
                 ca: int, vida_maxima: int, tamanho: str,posicao: list, tipo: str,
                 vida_atual: int):
        super().__init__(codigo, nome, forca, destreza, constituicao, inteligencia, sabedoria,
                         carisma, imagem, ca, vida_maxima, tamanho, posicao, vida_atual)
        self.__tipo = tipo

    def atacar(self, personagem: Personagem):
        pass
