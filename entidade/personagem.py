from abc import ABC, abstractmethod
import pygame
import random


class Personagem(ABC):
    @abstractmethod
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
        imagem: str,
        ca: int,
        vida_maxima: int,
        tamanho: str,
        vida_atual: int
    ):

        self.__id = id
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
        self.__tamanho = tamanho
        self.__imagem = imagem
        self.__posicao = self.define_posicao()
        self.__ca = ca
        self.__vida_maxima = vida_maxima
        self.__dano_causado = []
        self.__dano_sofrido = []
        self.__movimentacao_acumulado = 0
        self.__sorte = []
        self.__ataque_vantagem = False
        self.__ataque_desvantagem = False
        self.__sofre_ataque_vantagem = False
        self.__sofre_ataque_desvantagem = False
        self.__vida_atual = vida_atual
        self.__esta_vivo = True

    """
    getters
    """

    @property
    def id(self) -> int:
        return self.__id
  
    @property
    def nome(self):
        return self.__nome

    @property
    def forca(self):
        return self.__forca

    @property
    def mod_carisma(self):
        return self.__mod_carisma

    @property
    def ca(self):
        return self.__ca

    @property
    def mod_forca(self):
        return self.__mod_forca

    @property
    def destreza(self):
        return self.__destreza

    @property
    def mod_destreza(self):
        return self.__mod_destreza

    @property
    def constituicao(self):
        return self.__constituicao

    @property
    def mod_constituicao(self):
        return self.__mod_constituicao

    @property
    def inteligencia(self):
        return self.__inteligencia

    @property
    def mod_inteligencia(self):
        return self.__mod_inteligencia

    @property
    def sabedoria(self):
        return self.__sabedoria

    @property
    def mod_sabedoria(self):
        return self.__mod_sabedoria

    @property
    def carisma(self):
        return self.__carisma

    @property
    def imagem(self):
        return self.__imagem

    @property
    def posicao(self):
        return self.__posicao[:2]

    @posicao.setter
    def posicao(self, x: int, y: int):
        self.__posicao[0] = x
        self.__posicao[1] = y

    @property
    def atacar_vantagem(self):
        return self.__ataque_vantagem

    @property
    def atacar_desvantagem(self):
        return self.__ataque_desvantagem

    @property
    def sofre_ataque_vantagem(self):
        return self.__sofre_ataque_vantagem

    @property
    def sofre_ataque_desvantagem(self):
        return self.__sofre_ataque_desvantagem

    @property
    def dano_causado(self):
        return self.__dano_causado

    @property
    def dano_sofrido(self):
        return self.__dano_sofrido

    @property
    def dano_acumulado_inflingido(self):
        return self.__dano_causado

    @property
    def dano_acumulado_recebido(self):
        return self.__dano_sofrido

    @property
    def vida_atual(self):
        return self.__vida_atual

    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def esta_vivo(self):
        return self.__esta_vivo

    """
    setters
    """

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @forca.setter
    def forca(self, forca: int):
        if isinstance(forca, int):
            self.__forca = forca
            self.__mod_forca = self.calcula_modificador(forca)

    @destreza.setter
    def destreza(self, destreza: int):
        if isinstance(destreza, int):
            self.__destreza = destreza
            self.__mod_destreza = self.calcula_modificador(destreza)

    @constituicao.setter
    def constituicao(self, constituicao: int):
        if isinstance(constituicao, int):
            self.__constituicao = constituicao
            self.__mod_constituicao = self.calcula_modificador(constituicao)

    @inteligencia.setter
    def inteligencia(self, inteligencia: int):
        if isinstance(inteligencia, int):
            self.__inteligencia = inteligencia
            self.__mod_inteligencia = self.calcula_modificador(inteligencia)

    @sabedoria.setter
    def sabedoria(self, sabedoria: int):
        if isinstance(sabedoria, int):
            self.__sabedoria = sabedoria
            self.__mod_sabedoria = self.calcula_modificador(sabedoria)

    @carisma.setter
    def carisma(self, carisma: int):
        if isinstance(carisma, int):
            self.__carisma = carisma
            self.__mod_carisma = self.calcula_modificador(carisma)

    @ca.setter
    def ca(self, ca: int):
        if isinstance(ca, int):
            self.__ca = ca

    @tamanho.setter
    def tamanho(self, tamanho: str):
        if isinstance(tamanho, str):
            self.__tamanho = tamanho

    @vida_maxima.setter
    def vida_maxima(self, vida_maxima):
        if isinstance(vida_maxima, int):
            self.__vida_maxima = vida_maxima

    @atacar_vantagem.setter
    def atacar_vantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__ataque_vantagem = valor

    @atacar_desvantagem.setter
    def atacar_desvantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__ataque_desvantagem = valor

    @sofre_ataque_vantagem.setter
    def sofre_ataque_vantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__sofre_ataque_vantagem = valor

    @sofre_ataque_desvantagem.setter
    def sofre_ataque_desvantagem(self, valor: bool):
        if isinstance(valor, bool):
            self.__sofre_ataque_desvantagem = valor

    @vida_atual.setter
    def vida_atual(self, vida: int):
        if isinstance(vida, int):
            self.__vida_atual = vida

    @imagem.setter
    def imagem(self, imagem: pygame.image.load):
        if isinstance(imagem, pygame.Surface):
            self.__imagem = imagem

    @esta_vivo.setter
    def esta_vivo(self, situacao: bool):
        if isinstance(situacao, bool):
            self.__esta_vivo = situacao

    """
    methods
    """

    @staticmethod
    def calcula_modificador(atributo):
        return (atributo - 10) // 2

    def movimentar(self, posicao: list):
        self.__posicao = posicao
        self.__movimentacao_acumulado += ((posicao[0]**2 + posicao[1]**2)**(1/2))

    @staticmethod
    def realizar_teste(modificador: int):
        if isinstance(modificador, int):
            return random.randint(1, 20) + modificador

    def recebe_ataque(self, dano: int):
        if isinstance(dano, int):
            self.__vida_atual -= dano
            self.__dano_sofrido += dano

    def curar(self, vida: int):
        if isinstance(vida, int):
            self.__vida_atual += vida
            if self.__vida_atual > self.__vida_maxima:
                self.__vida_atual = self.__vida_maxima

    def define_pygame_imagem(self, imagem_pygame=None):
        if not imagem_pygame:
            imagem_pygame = pygame.image.load("tokens/" + self.__imagem + '.png')

        proporcoes = {
            'Padrao': (100, 100),
            'Grande': (200, 200),
            'Enorme': (300, 300),
            'Colossal': (400, 400),
        }

        if self.tamanho in proporcoes:
            proporcao = proporcoes[self.tamanho]
        else:
            proporcao = proporcoes['Padrao']

        return pygame.transform.scale(imagem_pygame, proporcao)

    def define_posicao(self):
        imagem_pygame = pygame.image.load("tokens/" + self.__imagem + '.png')
        posicao = imagem_pygame.get_rect()
        posicao[0] = 100 * (self.id % 10)
        posicao[1] = 100 * ((self.id * 10) // 10)
        return posicao
