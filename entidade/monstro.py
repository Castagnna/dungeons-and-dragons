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

    def atacar(self, personagem: Personagem):
        self.mostrar_ataques()
        while True:
            try:
                selecao = int(input('Digite o número correspondente ao ataque: '))
                ataque = self.__ataques[selecao]
                break
            except:
                print('Valor inválido, favor digitar o número referente ao ataque')
        if (random.randint(1,20) + ataque.acerto) > personagem.ca:
            contador = 0
            for i in range(ataque.quantidade_dado):
                contador += random.randint(1,ataque.numero_faces)
            personagem.recebe_ataque(contador + ataque.dano_bonus)
