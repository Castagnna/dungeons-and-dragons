from entidade.personagem import Personagem
from entidade.arma import Arma
from entidade.magia import Magia
import pygame


class Jogador(Personagem):
    def __init__(self, id: int, nome: str, forca: int,
                 destreza: int, constituicao: int, inteligencia: int,
                 sabedoria: int, carisma: int, imagem: pygame.image.load,
                 ca: int, vida_maxima: int,
                 tamanho: str, vida_atual: int,
                 nome_jogador: str, level: int, experiencia: int,proficiencia: int, cd: int):
    
        super().__init__(id, nome, forca, destreza, constituicao, inteligencia, sabedoria,
                         carisma, imagem, ca, vida_maxima, tamanho, vida_atual)
        self.__nome_jogador = nome_jogador
        self.__level = level
        self.__experiencia = experiencia
        self.__espaco_magia = {0: float('inf'), 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        self.__proficiencia = proficiencia
        self.__cd = cd
        self.__armas = []
        self.__magias = []
        self.__raca = None

    """
    getters
    """

    @property
    def nome_jogador(self):
        return self.__nome_jogador

    @property
    def raca(self):
        return self.__raca

    @property
    def proficiencia(self):
        return self.__proficiencia

    @property
    def armas(self):
        return self.__armas

    @property
    def magias(self):
        return self.__magias

    @property
    def level(self):
        return self.__level

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def cd(self):
        return self.__cd

    """
    setters
    """

    @nome_jogador.setter
    def nome_jogador(self, nome_jogador: str):
        if isinstance(nome_jogador, str):
            self.__nome_jogador: nome_jogador

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca

    @proficiencia.setter
    def proficiencia(self, proficiencia: int):
        if isinstance(proficiencia, int):
            self.__proficiencia = proficiencia

    @cd.setter
    def cd(self, cd):
        if isinstance(cd, int):
            self.__cd = cd

    @experiencia.setter
    def experiencia(self, experiencia):
        if isinstance(experiencia, int):
            self.__experiencia = experiencia

    @level.setter
    def level(self, level):
        if isinstance(level, int):
            self.__level = level

    """
    methods
    """

    def adiciona_arma(self, arma: Arma):
        if isinstance(arma, Arma):
            self.__armas.append(arma)

    def remove_arma(self, arma: Arma):
        if arma in self.__armas:
            self.__armas.remove(arma)

    def vincula_magia(self, magia: Magia):
        if isinstance(magia, Magia):
            self.__magias.append(magia)

    def desvincula_magia(self, magia: Magia):
        if magia in self.__magias:
            self.__magias.remove(magia)

    def get_espaco_magia(self, circulo: int):
        if isinstance(circulo, int):
            return self.__espaco_magia[circulo]

    def set_espaco_magia(self, circulo: int, quantidade: int):
        if isinstance(circulo, int) and isinstance(quantidade, int):
            self.__espaco_magia[circulo] = quantidade

    def recebe_experiencia(self, experiencia: int):
        if isinstance(experiencia, int):
            self.__experiencia += experiencia
