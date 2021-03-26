from controle.controladorGenerico import ControladorGenerico
from limite.telaArma import TelaArma
from entidade.arma import Arma
# from entidade.monstro import Monstro


class ControladorArma(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorArma, self).__init__(TelaArma(self))
        self.__controlador_principal = controlador_principal
        self.__armas = []
        self.__counta_armas = 0

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def armas(self):
        return self.__armas

    def mostra_armas(self):
        # lista_de_armas = [(arma.id, arma.nome) for arma in self.__armas]
        self.tela.mostra_armas(self.__armas)

    def cria_nova_arma(self):
        dados = self.tela.pega_dados_da_arma()
        novo_arma = Arma(
            id=self.__counta_armas,
            **dados
        )
        self.__armas.append(novo_arma)
        self.__counta_armas += 1

    def mostra_tela(self):

        funcoes = {
            -1: self.mostra_tela,
            0: self.finaliza_programa,
            1: self.cria_nova_arma,
            2: self.mostra_armas,
        }

        super(ControladorArma, self).mostra_tela(funcoes)
