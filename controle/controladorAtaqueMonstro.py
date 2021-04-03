from controle.controladorGenerico import ControladorGenerico
from limite.telaAtaqueMonstro import TelaAtaqueMonstro


class ControladorAtaqueMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorAtaqueMonstro, self).__init__(TelaAtaqueMonstro(self))

    def mostra_tela(self, funcoes: dict):
        pass
