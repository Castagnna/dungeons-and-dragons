from controle.controladorGenerico import ControladorGenerico
from limite.telaPersonagem import TelaPersonagem
from entidade.jogador import Jogador
from entidade.monstro import Monstro


class ControladorPersonagem(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorPersonagem, self).__init__(TelaPersonagem(self))
        self.__controlador_principal = controlador_principal
        self.__jogadores = []
        self.__counta_personagens = 0
        self.__monstros = []

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    def cria_novo_jogador(self):
        dados = self.tela.pega_dados_do_jogador()
        novo_jogador = Jogador(
            codigo=self.__counta_personagens,
            imagem=None,
            posicao=[0,0],
            **dados
        )
        self.__counta_personagens += 1
        self.__jogadores.append(novo_jogador)
        return -1

    def iniciar_combate(self):
        print("Batalha")
        return -1

    def mostra_tela(self):

        funcoes = {
            1: self.cria_novo_jogador,
            2: self.iniciar_combate,
            88: self.controlador_principal.mostra_tela,
        }

        super(ControladorPersonagem, self).mostra_tela(funcoes)
