from controle.controladorGenerico import ControladorGenerico
from limite.telaAtaqueMonstro import TelaAtaqueMonstro
from entidade.ataqueMonstro import AtaqueMonstro


class ControladorAtaqueMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorAtaqueMonstro, self).__init__(TelaAtaqueMonstro(self))
        self.__controlador_principal = controlador_principal
        self.__ataques_monstro = []

    def mostra_tela(self, funcoes: dict):
        pass

    def cadastrar_ataque_monstro(self):
        nome, quantidade_dado, numero_faces, dano_bonus, teste, acerto, cd = self.__tela.cadastrar_ataque()
        ataque = AtaqueMonstro(nome, quantidade_dado, numero_faces, dano_bonus, acerto, teste, cd)
        self.__ataques_monstro = ataque