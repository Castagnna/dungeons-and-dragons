from controle.controladorGenerico import ControladorGenerico
from controle.controladorJogador import ControladorJogador
from controle.controladorMonstro import ControladorMonstro
from controle.controladorArma import ControladorArma
from controle.controladorAtaqueMonstro import ControladorAtaqueMonstro
from controle.controladorBackground import ControladorBackground
from limite.telaPrincipal import TelaPrincipal
import pygame


class ControladorPrincipal(ControladorGenerico):
    def __init__(self):
        super(ControladorPrincipal, self).__init__(TelaPrincipal(self))
        self.__controlador_arma = ControladorArma(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_ataque_monstro = ControladorAtaqueMonstro(self)
        self.__controlador_monstro = ControladorMonstro(self)
        self.__controlador_background = ControladorBackground(self)
        self.__controlador_jogador.add_controlador_monstro(self.__controlador_monstro)
        # self.__retangulos = [pygame.rect.Rect(0, 0, 100, 1000), pygame.rect.Rect(0, 0, 1800, 100)]
        # self.__visualizacao = pygame.display.set_mode((1800, 1000))

    """
    getters
    """

    @property
    def controlador_arma(self):
        return self.__controlador_arma

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def controlador_ataque_monstro(self):
        return self.__controlador_ataque_monstro

    @property
    def controlador_monstro(self):
        return self.__controlador_monstro

    """
    setters
    """

    @controlador_jogador.setter
    def controlador_jogador(self, controlador):
        self.__controlador_jogador = controlador

    @controlador_arma.setter
    def controlador_arma(self, controlador):
        self.__controlador_arma = controlador

    @controlador_monstro.setter
    def controlador_monstro(self, controlador):
        self.__controlador_monstro = controlador

    """
    methods
    """

    def iniciar_sistema(self):
        self.mostra_tela()

    def opcoes_jogador(self):
        self.__controlador_jogador.mostra_tela()

    def opcoes_monstro(self):
        self.__controlador_monstro.mostra_tela()

    def opcoes_arma(self):
        self.__controlador_arma.mostra_tela()

    def opcoes_ataque_monstro(self):
        self.__controlador_ataque_monstro.mostra_tela()

    def opcoes_background(self):
        self.__controlador_background.mostra_tela()

    def mostra_tela(self):

        funcoes = {
            1: self.opcoes_jogador,
            2: self.opcoes_monstro,
            3: self.opcoes_arma,
            4: self.opcoes_ataque_monstro,
            5: self.opcoes_background,
        }

        super(ControladorPrincipal, self).mostra_tela(funcoes)

    def atualizar_visualizacao(self):
        self.__visualizacao.fill((0, 0, 0))
        self.__visualizacao.blit(self.__controlador_background.mostra_mapa(),
                                 self.__controlador_background.mostra_posicao_mapa())
        for monstro in range(len(self.__controlador_monstro.monstros)):
            self.__visualizacao.blit(self.__controlador_monstro.mostra_imagem(monstro),
                                     self.__controlador_monstro.mostrar_posicao(monstro))
        for jogador in range(len(self.__controlador_jogador.jogadores)):
            self.__visualizacao.blit(self.__controlador_jogador.mostra_imagem(jogador),
                                     self.__controlador_jogador.mostrar_posicao(jogador))
        pygame.display.flip()

    def movimentar_mapa(self, x: int, y: int):
        self.__controlador_jogador.mapa_moveu(x, y)
        self.__controlador_monstro.mapa_moveu(x, y)
        self.atualizar_visualizacao()