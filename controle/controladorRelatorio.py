from controle.controladorGenerico import ControladorGenerico
from limite.telaRelatorio import TelaRelatorio


class ControladorRelatorio(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorRelatorio, self).__init__(TelaRelatorio(self))
        self.__controlador_principal = controlador_principal
        self.__eventos_combate = []
        self.__counta_eventos = 0

    """
    getters
    """

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def eventos_combate(self):
        return self.__eventos_combate

    @property
    def counta_eventos(self):
        return self.__counta_eventos

    """
    setters
    """

    """
    methods
    """

    def registra_combate(self, atacante, defensor, dano: int):
        combate = (
            self.__counta_eventos,
            atacante,
            defensor,
            dano,
        )
        self.__eventos_combate.append(combate)
        self.__counta_eventos += 1
        self.tela.executado_com_sucesso()

    def relatorio_combates(self):
        self.tela.cria_relatorio(self.__eventos_combate)

    def mostra_tela(self):

        funcoes = {
            1: self.relatorio_combates,
        }

        super(ControladorRelatorio, self).mostra_tela(funcoes)
