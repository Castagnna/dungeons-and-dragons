from controle.controladorGenerico import ControladorGenerico
from limite.telaMonstro import TelaMonstro


class ControladorMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorMonstro, self).__init__()
        self.__controlador_principal = controlador_principal
        self.__tela = TelaMonstro(self)
        self.__jogadores = []

    def equipa_arma(self):
        print("equipa arma")
        return None

    def mostra_tela(self):

        funcoes = {
            -1: self.mostra_tela,
            0: self.finaliza_programa,
            1: self.equipa_arma,
        }

        while True:
            opcao_selecionada = self.__tela.mostra_opcoes()
            funcao_selecionada = funcoes[opcao_selecionada]
            funcao_selecionada()
