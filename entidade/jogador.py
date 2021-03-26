from entidade.personagem import Personagem
from entidade.arma import Arma
from entidade.magia import Magia
from entidade.monstro import Monstro
import pygame


class Jogador(Personagem):
    def __init__(self, codigo: int, nome: str, forca: int, destreza: int, constituicao: int, inteligencia: int,
                 sabedoria: int, carisma: int, imagem: pygame.image.load, ca: int, vida_maxima: int,
                 tamanho: str,posicao: list, vida_atual: int, nome_jogador: str, level: int, experiencia: int)
    
        super().__init__(codigo, nome, forca, destreza, constituicao, inteligencia, sabedoria,
                         carisma, imagem, ca, vida_maxima, tamanho, posicao, vida_atual)
        self.__nome_jogador = nome_jogador
        self.__level = level
        self.__experiencia = experiencia
        self.__raca = raca
        self.__espaco_magia = dict()
        self.__proficiencia = 0
        self.__cd = 0
        self.__armas = []
        self.__magias = []

    @property
    def nome_jogador(self):
        return self.__nome_jogador

    @nome_jogador.setter
    def nome_jogador(self, nome_jogador: str):
        if isinstance(nome_jogador, str):
            self.__nome_jogador: nome_jogador

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca

    def trocar_arma(self, arma: Arma):
        # TODO: implementar
        pass

    def get_espaco_magia(self, circulo: int):
        if isinstance(circulo, int):
            return self.__espaco_magia[circulo]

    def set_espaco_magia(self, circulo: int, quantidade: int):
        if isinstance(circulo, int) and isinstance(quantidade, int):
            self.__espaco_magia[circulo] = quantidade

    def lancar_magia(self, magia: Magia):
        # TODO: implementar
        pass

    @property
    def proficiencia(self):
        return self.__proficiencia

    @proficiencia.setter
    def proficiencia(self, proficiencia: int):
        if isinstance(proficiencia, int):
            self.__proficiencia = proficiencia

    def atacar(self, personagem: Personagem): # implementar
        pass

    def calcula_cd(self):
        # TODO: implementar
        pass

    def recebe_experiencia(self, experiencia: int):
        if isinstance(experiencia, int):
            self.__experiencia += experiencia
