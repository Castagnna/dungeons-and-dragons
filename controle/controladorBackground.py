from dao.backgroundDAO import BackgroundDAO

from entidade.background import Background

from limite.telaBackground import TelaBackground
from limite.telaBackgroundImagem import TelaBackgroundImagem
from limite.telaBackgroundMovimentar import TelaBackgroundMovimentar
from excecao.imagemException import TelaImagemException
import pygame


class ControladorBackground:
    def __init__(self, controlador):
        self.__tela = TelaBackground(self)
        self.__tela_imagem = TelaBackgroundImagem(self)
        self.__tela_movimentar = TelaBackgroundMovimentar(self)
        self.__dao = BackgroundDAO()
        self.__erro_imagem = TelaImagemException()
        self.__controlador_principal = controlador
        self.__background = Background(pygame.image.load('mapas/Branco.png'), [0,0,5000,5000])

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def background(self):
        return self.__background

    def mostra_tela(self):

        evento, _= self.__tela.mostra_tela()

        if evento == 'VOLTAR':
            self.__tela.fecha_tela()
            self.__controlador_principal.mostra_tela()

        funcoes = {
            'INSERI_MAPA': self.inseri_imagem,
            'MOVIMENTA_MAPA': self.movimentar_mapa
        }

        try:
            self.__tela.fecha_tela()
            funcoes[evento]()
            self.mostra_tela()
        except KeyError:
            pass


    def inseri_imagem(self, evento='CONFIRMAR', valores: dict=None):
        mostra_tela = True
        while mostra_tela:
            if not valores:
                evento, valores = self.__tela_imagem.mostra_tela()
            try:
                if evento == 'CONFIRMAR':
                    imagem = pygame.image.load('mapas/' + valores[0] + '.png')
                    posicao = imagem.get_rect()
                    self.__background = Background(imagem, posicao)
                    mostra_tela = False
                    self.__tela_imagem.popup_sucesso(titulo='Background criado/alterado')
                    self.__controlador_principal.atualizar_visualizacao()
                    self.__tela_imagem.fecha_tela()
                elif evento == 'CANCELAR' or evento == None:
                    mostra_tela = False
                    self.__tela_imagem.fecha_tela()
            except FileNotFoundError:
                self.__tela_imagem.fecha_tela()
                _ = self.__erro_imagem.mostra_erro()
                self.__erro_imagem.fecha_tela()
                valores = None


    def movimentar_mapa(self):
        evento, _ = self.__tela_movimentar.mostra_tela()
        dicionario = {1: [0, -100],
                      2: [-100, 0],
                      3: [100, 0],
                      4: [0, 100]}
        valores = dicionario[int(evento)]
        self.__background.movimentar(valores)
        self.__controlador_principal.movimentar_mapa(valores)

    def mostra_mapa(self):
        return self.__background.imagem

    def mostra_posicao_mapa(self):
        return self.__background.posicao
