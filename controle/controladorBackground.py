from controle.controladorGenerico import ControladorGenerico
from entidade.background import Background
from limite.telaBackground import TelaBackground


class ControladorBackground(ControladorGenerico):
    def __init__(self, principal):
        super().__init__(TelaBackground(self))
        self.__controlador_principal = principal
        self.__background = ''

    def movimentar_mapa(self):
        valores = self.__tela.movimenta_mapa()
        self.__background.movimentar(valores)
        self.__controlador_principal.movimentar_mapa()

    def inseri_imagem(self):
        imagem = self.__tela.pede_imagem('mapas/')
        posicao = imagem.get_rect()
        self.__background = Background(imagem, posicao)

    def mostra_tela(self):
        lista_opcoes = {
            1: self.inseri_imagem,
            2: self.movimentar_mapa,
        }
        opcao = self.__tela.mostra_opcoes()
        try:
            lista_opcoes[opcao]()
        except:
            print('Você não pode movimentar algo que ainda não existe, favor inserir um mapa')