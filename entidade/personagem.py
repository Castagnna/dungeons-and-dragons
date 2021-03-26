from abc import ABC, abstractmethod
import pygame
import random


class Personagem(ABC):

    def __init__(self, codigo: int, nome: str, forca: int, destreza: int, constituicao: int,
                 inteligencia: int, sabedoria: int, carisma: int, imagem: pygame.image.load,
                 ca: int, vida_maxima: int, tamanho: str, posicao: list, vida_atual: int):

        self.__codigo = codigo
        self.__nome = nome
        self.__forca = forca
        self.__mod_forca = self.calcula_modificador(forca)
        self.__destreza = destreza
        self.__mod_destreza = self.calcula_modificador(destreza)
        self.__constituicao = constituicao
        self.__mod_constituicao = self.calcula_modificador(constituicao)
        self.__inteligencia = inteligencia
        self.__mod_inteligencia = self.calcula_modificador(inteligencia)
        self.__sabedoria = sabedoria
        self.__mod_sabedoria = self.calcula_modificador(sabedoria)
        self.__carisma = carisma
        self.__mod_carisma = self.calcula_modificador(carisma)
        self.__imagem = imagem
        self.__ca = ca
        self.__vida_maxima = vida_maxima
        self.__tamanho = tamanho
        self.__posicao = posicao
        self.__dano_causado = 0
        self.__dano_sofrido = 0
        self.__movimentacao_acumulado = 0
        self.__sorte = []
        self.__ataque_vantagem = False
        self.__ataque_desvantagem = False
        self.__sofre_ataque_vantagem = False
        self.__sofre_ataque_desvantagem = False
        self.__vida_atual = vida_atual

    def calcula_modificador(self, atributo):
        return (atributo - 10) // 2

    @property
    def forca(self):
        return self.__forca

    @forca.setter
    def forca(self, forca: int):
        if isinstance(forca, int):
            self.__forca = forca
            self.__mod_forca = self.calcula_modificador(forca)

    @property
    def mod_forca(self):
        return self.__mod_forca

    @property
    def destreza(self):
        return self.__destreza

    @destreza.setter
    def destreza(self, destreza: int):
        if isinstance(destreza, int):
            self.__destreza = destreza
            self.__mod_destreza = self.calcula_modificador(destreza)

    @property
    def mod_destreza(self):
        return self.__mod_destreza

    @property
    def constituicao(self):
        return self.__constituicao

    @constituicao.setter
    def constituicao(self, constituicao: int):
        if isinstance(constituicao, int):
            self.__constituicao = constituicao
            self.__mod_constituicao = self.calcula_modificador(constituicao)

    @property
    def mod_constituicao(self):
        return self.__mod_constituicao

    @property
    def inteligencia(self):
        return self.__inteligencia

    @inteligencia.setter
    def inteligencia(self, inteligencia: int):
        if isinstance(inteligencia, int):
            self.__inteligencia = inteligencia
            self.__mod_inteligencia = self.calcula_modificador(inteligencia)

    @property
    def mod_inteligencia(self):
        return self.__mod_inteligencia

    @property
    def sabedoria(self):
        return self.__sabedoria

    @sabedoria.setter
    def sabedoria(self, sabedoria: int):
        if isinstance(sabedoria, int):
            self.__sabedoria = sabedoria
            self.__mod_sabedoria = self.calcula_modificador(sabedoria)

    @property
    def mod_sabedoria(self):
        return self.__mod_sabedoria

    @property
    def carisma(self):
        return self.__carisma

    @carisma.setter
    def carisma(self, carisma: int):
        if isinstance(carisma, int):
            self.__carisma = carisma
            self.__mod_carisma = self.calcula_modificador(carisma)

    @property
    def mod_carisma(self):
        return self.__mod_carisma

    @property
    def ca(self):
        return self.__ca

    @ca.setter
    def ca(self, ca: int):
        if isinstance(ca, int):
            self.__ca = ca

    def movimentar(self, posicao: list): #ajustar conforme método de localização
        self.__posicao = posicao
        self.__movimentacao_acumulado += ((posicao[0]**2 + posicao[1]**2)**(1/2))

    @abstractmethod
    def atacar(self, personagem):
        pass

    @property
    def atacar_vantagem(self):
        return self.__ataque_vantagem

    @atacar_vantagem.setter
    def atacar_vantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__ataque_vantagem = valor

    @property
    def atacar_desvantagem(self):
        return self.__ataque_desvantagem

    @atacar_desvantagem.setter
    def atacar_desvantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__ataque_desvantagem = valor

    @property
    def sofre_ataque_vantagem(self):
        return self.__sofre_ataque_vantagem

    @sofre_ataque_vantagem.setter
    def sofre_ataque_vantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__sofre_ataque_vantagem = valor

    @property
    def sofre_ataque_desvantagem(self):
        return self.__sofre_ataque_desvantagem

    @sofre_ataque_desvantagem.setter
    def sofre_ataque_desvantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__sofre_ataque_desvantagem = valor

    @property
    def dano_acumulado_inflingido(self):
        return self.__dano_causado

    @property
    def dano_acumulado_recebido(self):
        return self.__dano_sofrido

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    def realizar_teste(self, modificador: int):
        if isinstance(modificador, int):
            return (random.randint(1, 20) + modificador)

    def recebe_ataque(self, dano: int):
        if isinstance(dano, int):
            self.__vida_atual -= dano
            self.__dano_sofrido += dano

    def curar(self, vida: int):
        if isinstance(vida, int):
            self.__vida_atual += vida
            if self.__vida_atual > self.__vida_maxima:
                self.__vida_atual = self.__vida_maxima
