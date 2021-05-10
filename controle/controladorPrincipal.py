from controle.controladorGenerico import ControladorGenerico
from controle.controladorJogador import ControladorJogador
from controle.controladorMonstro import ControladorMonstro
from controle.controladorArma import ControladorArma
from controle.controladorAtaqueMonstro import ControladorAtaqueMonstro
from controle.controladorBackground import ControladorBackground
from controle.controladorRelatorio import ControladorRelatorio

from limite.principal.telaPrincipal import TelaPrincipal
# import pygame


class ControladorPrincipal(ControladorGenerico):
    def __init__(self):

        # pygame.init()

        self.__tela_principal = TelaPrincipal(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__controlador_arma = ControladorArma(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_ataque_monstro = ControladorAtaqueMonstro(self)
        self.__controlador_monstro = ControladorMonstro(self)
        self.__controlador_background = ControladorBackground(self)
        self.__controlador_jogador.add_controlador_monstro(self.__controlador_monstro)
        # self.__retangulos = [pygame.rect.Rect(0, 0, 100, 1000), pygame.rect.Rect(0, 0, 1800, 100)]
        # self.__fonte = pygame.font.SysFont(None, 55)
        # self.__letras = ('A','B','C','D','E','F','G','H','I','J',
        #                  'K','L','M','N','O','P', 'Q', 'R', 'S',
        #                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        # self.__numeros = ('1','2','3','4','5','6','7','8', '9')
        # self.__visualizacao = ''

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

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

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

    def finaliza_programa(self):
        evento = self.__tela_principal.yes_or_no("Deseja finalizar o programa?")

        if evento == "Yes":
            exit(0)

        self.__tela_principal.fecha_tela()
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

    def opcoes_relatorio(self):
        self.__controlador_relatorio.mostra_tela()

    def mostra_tela(self):

        evento, _ = self.__tela_principal.mostra_tela()

        telas = {
            "JOGADOR": self.opcoes_jogador,
            "MONSTRO": self.opcoes_monstro,
            "ARMA": self.opcoes_arma,
            "ATAQUE_MONSTRO": self.opcoes_ataque_monstro,
            "BACKGROUND": self.opcoes_background,
            "RELATORIO": self.opcoes_relatorio,
            "FINALIZAR": self.finaliza_programa,
            None: self.finaliza_programa,
        }

        try:
            self.__tela_principal.fecha_tela()
            telas[evento]()
        except KeyError:
            pass

    
    # def grid(self): # desenha o grid
    #     lista_inicio = [100,100]
    #     lista_x = [100, 1000] # ajustar de acordo com a resolução
    #     lista_y = [1800, 100] # ajustar de acordo com a resolução
    #     while lista_inicio[0] <= 1800: # ajustar de acordo com a resolução
    #         pygame.draw.line(self.__visualizacao, (0,0,0), lista_inicio, lista_x, 1)
    #         lista_inicio[0] += 100
    #         lista_x[0] += 100
    #     lista_inicio[0] = 100
    #     while lista_inicio[1] <= 1000: # ajustar de acordo com a resolução
    #         pygame.draw.line(self.__visualizacao, (0,0,0), lista_inicio, lista_y, 1)
    #         lista_inicio[1] += 100
    #         lista_y[1] += 100

    # def posicoes_grid(self): # adicionando orientações do grid
    #     marcador_letras = 0
    #     posicao_letras = [136,36]
    #     marcador_numeros = 0
    #     posicao_numeros = [36,136]
    #     while posicao_letras[0] < 1800:
    #         letra = self.__fonte.render(self.__letras[marcador_letras], True, (0,0,0))
    #         self.__visualizacao.blit(letra, posicao_letras)
    #         marcador_letras += 1
    #         posicao_letras[0] += 100
    #     while posicao_numeros[1] < 1000:
    #         numero = self.__fonte.render(self.__numeros[marcador_numeros], True, (0,0,0))
    #         self.__visualizacao.blit(numero, posicao_numeros)
    #         marcador_numeros += 1
    #         posicao_numeros[1] += 100

    # def atualizar_visualizacao(self):
    #     self.__visualizacao = pygame.display.set_mode((1800, 1000))
    #     pygame.display.set_caption('Trabalho DSO')
    #     self.__visualizacao.fill((0, 0, 0))
    #     self.__visualizacao.blit(self.__controlador_background.mostra_mapa(),
    #                         self.__controlador_background.mostra_posicao_mapa())

    #     for monstro in self.__controlador_monstro.monstros:
    #         imagem_pygame = monstro.define_pygame_imagem()
    #         posicao = monstro.posicao
    #         self.__visualizacao.blit(imagem_pygame, posicao)

    #     for jogador in self.__controlador_jogador.jogadores:
    #         imagem_pygame = jogador.define_pygame_imagem()
    #         posicao = jogador.posicao
    #         self.__visualizacao.blit(imagem_pygame, posicao)

    #     self.grid()
    #     pygame.draw.rect(self.__visualizacao, (255, 255, 255), self.__retangulos[0])
    #     pygame.draw.rect(self.__visualizacao, (255, 255, 255), self.__retangulos[1])
    #     self.posicoes_grid()
    #     pygame.display.flip()

    # def movimentar_mapa(self, valores: list):
    #     self.__controlador_jogador.mapa_moveu(valores[0], valores[1])
    #     self.__controlador_monstro.mapa_moveu(valores[0], valores[1])
    #     self.atualizar_visualizacao()
