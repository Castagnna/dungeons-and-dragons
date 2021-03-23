from controle.controladorGenerico import ControladorGenerico
from limite.telaPrincipal import TelaPrincipal


class ControladorPrincipal(ControladorGenerico):
    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)

    def iniciar(self):
        self.__tela_principal.mostra_opcoes()
