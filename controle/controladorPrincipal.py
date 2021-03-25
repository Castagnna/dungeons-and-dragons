from controle.controladorGenerico import ControladorGenerico
from controle.controladorPersonagem import ControladorPersonagem
from controle.controladorArma import ControladorArma
from limite.telaPrincipal import TelaPrincipal


class ControladorPrincipal(ControladorGenerico):
    def __init__(self):
        super(ControladorPrincipal, self).__init__(TelaPrincipal(self))
        self.__controlador_personagem = ControladorPersonagem(self)
        self.__controlador_arma = ControladorArma(self)

    def iniciar_sistema(self) -> int:
        return self.mostra_tela()

    def opcoes_personagem(self):
        return self.__controlador_personagem.mostra_tela()

    def opcoes_arma(self):
        return self.__controlador_arma.mostra_tela()

    def mostra_tela(self):

        funcoes = {
            -1: self.mostra_tela,
            0: self.finaliza_programa,
            1: self.opcoes_personagem,
            2: self.opcoes_arma,
        }

        super(ControladorPrincipal, self).mostra_tela(funcoes)
