from controle.controladorGenerico import ControladorGenerico
from controle.controladorJogador import ControladorJogador
from controle.controladorMonstro import ControladorMonstro
from limite.telaPrincipal import TelaPrincipal


class ControladorPrincipal(ControladorGenerico):
    def __init__(self):
        super(ControladorPrincipal, self).__init__()
        self.__tela = TelaPrincipal(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_monstro = ControladorMonstro(self)

    def iniciar_sistema(self) -> int:
        return self.mostra_tela()

    def opcoes_jogador(self):
        return self.__controlador_jogador.mostra_tela()

    def opcoes_monstro(self):
        return self.__controlador_monstro.mostra_tela()

    def mostra_tela(self):

        funcoes = {
            -1: self.mostra_tela,
            0: self.finaliza_programa,
            1: self.opcoes_jogador,
            2: self.opcoes_monstro,
        }

        while True:
            opcao_selecionada = self.__tela.mostra_opcoes()
            funcao_selecionada = funcoes[opcao_selecionada]
            funcao_selecionada()
