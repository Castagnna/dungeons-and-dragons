from entidade.personagem import Personagem
from entidade.ataqueMonstro import AtaqueMonstro
import random
import pygame


class Monstro(Personagem):
    def __init__(
        self,
        id: int,
        nome: str,
        forca: int,
        destreza: int,
        constituicao: int,
        inteligencia: int,
        sabedoria: int,
        carisma: int,
        imagem: pygame.image.load,
        ca: int,
        vida_maxima: int,
        tamanho: str,
        posicao: list,
        tipo: str,
        experiencia: int,
        vida_atual: int
    ):
        super().__init__(
            id, nome, forca, destreza, constituicao, inteligencia,
            sabedoria, carisma, imagem, ca, vida_maxima, tamanho,
            posicao, vida_atual
        )
        self.__tipo = tipo
        self.__ataques = []
        self.__experiencia = experiencia
        self.__atacado_por = set()

    """
    getters
    """

    @property
    def ataques(self) -> list:
        return self.__ataques

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def experiencia(self) -> int:
        return self.__experiencia

    """
    setters
    """

    """
    methods
    """

    def inserir_ataque(self, ataque: AtaqueMonstro):
        if isinstance(ataque, AtaqueMonstro):
            self.__ataques.append(ataque)

    def mostrar_ataques(self):
        for i in range(len(self.__ataques)):
            print(str(i) + ' - ' + self.__ataques[i].nome)

    def remover_ataque(self):
        self.mostrar_ataques()
        while True:
            try:
                excluir = int(input('Digite o número correspondente ao ataque que deseja excluir: '))
                self.__ataques.pop(excluir)
                return
            except:
                print('Valor inválido, favor digitar o número referente ao ataque que deseja excluir')

    @property
    def atacado_por(self):
        return self.__atacado_por

    @property
    def tipo(self):
        return self.__tipo

    @property
    def experiencia(self):
        return self.__experiencia

    @atacado_por.setter
    def atacado_por(self, atacado):
        if isinstance(atacado, set):
            self.__atacado_por = atacado

    @property
    def ataques(self):
        return self.__ataques

    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo

    @experiencia.setter
    def experiencia(self, experiencia: int):
        if isinstance(experiencia, int):
            self.__experiencia = experiencia

    def adiciona_atacante(self, atacante):
        self.__atacado_por.add(atacante)

