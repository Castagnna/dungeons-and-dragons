from controle.controladorGenerico import ControladorGenerico
from entidade.background import Background
from limite.telaBackground import TelaBackground
import pygame

class ControladorBackground(ControladorGenerico):
    def __init__(self, principal):
        super(ControladorBackground, self).__init__(TelaBackground(self))
        self.__controlador_principal = principal
        self.__background = Background(pygame.image.load('mapas/Branco.png'), (0,0,5000,5000))


    def movimentar_mapa(self):
        valores = self.tela.movimenta_mapa()
        try:
            valores[0], valores[1] = valores[0] - 100, valores[1] - 100
            self.__background.movimentar(valores)
            self.__controlador_principal.movimentar_mapa(valores)
        except TypeError:
            self.tela.erro_movimentacao()

    def inseri_imagem(self):
        imagem = self.tela.pega_imagem('mapas/')
        posicao = imagem.get_rect()
        self.__background = Background(imagem, posicao)

    def mostra_tela(self):

        funcoes = {
            1: self.inseri_imagem,
            2: self.movimentar_mapa
        }
        super(ControladorBackground, self).mostra_tela(funcoes)
        self.__controlador_principal.atualizar_visualizacao()

    def mostra_mapa(self):
        return self.__background.imagem

    def mostra_posicao_mapa(self):
        return self.__background.posicao