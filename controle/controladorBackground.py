from controle.controladorGenerico import ControladorGenerico
from entidade.background import Background
from limite.telaBackground import TelaBackground

class ControladorBackground(ControladorGenerico):
    def __init__(self, principal):
        super(ControladorBackground, self).__init__(TelaBackground(self))
        self.__controlador_principal = principal
        self.__background = ''


    def movimentar_mapa(self):
        valores = self.__tela.movimenta_mapa()
        self.__background.movimentar(valores)
        self.__controlador_principal.movimentar_mapa()

    def inseri_imagem(self):
        imagem = self.tela.pede_imagem('mapas/')
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
        return self.__background.imagem()

    def mostra_posicao_mapa(self):
        return self.__background.posicao()