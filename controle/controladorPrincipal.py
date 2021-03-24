from controle.controladorGenerico import ControladorGenerico
from controle.controladorPersonagem import ControladorPersonagem
from limite.telaPrincipal import TelaPrincipal


class ControladorPrincipal(ControladorGenerico):
    def __init__(self):
        super(ControladorPrincipal, self).__init__()
        self.__tela = TelaPrincipal(self)
        self.__controlador_personagem = ControladorPersonagem(self)

    def iniciar_sistema(self) -> int:
        return self.mostra_tela()

    def opcoes_personagem(self):
        return self.__controlador_personagem.mostra_tela()

    def mostra_tela(self):

        funcoes = {
            -1: self.mostra_tela,
            0: self.finaliza_programa,
            1: self.opcoes_personagem,
        }

        while True:
            opcao_selecionada = self.__tela.mostra_opcoes()
            funcao_selecionada = funcoes[opcao_selecionada]
            funcao_selecionada()
