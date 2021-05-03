from controle.controladorGenerico import ControladorGenerico
from limite.telaRelatorio import TelaRelatorio
from dao.combateContadorDAO import CombateContadorDAO
from dao.combateDAO import CombateDAO


class ControladorRelatorio(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorRelatorio, self).__init__(TelaRelatorio(self))
        self.__controlador_principal = controlador_principal
        self.__dao = CombateDAO()
        self.__dao_contador = CombateContadorDAO()

    """
    getters
    """

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def eventos_combate(self):
        return self.__dao.get_all()

    @property
    def counta_eventos(self):
        return self.__dao_contador.get()

    """
    setters
    """

    """
    methods
    """

    def registra_combate(self, atacante, defensor, dano: int):
        combate = {
            "id": self.__dao_contador.get() + 1,
            "atacante": atacante,
            "defensor": defensor,
            "dano": dano,
        }
        self.__dao.add(combate)
        self.__dao_contador.add(1)
        self.tela.executado_com_sucesso()

    def relatorio_combates(self):
        self.tela.cria_relatorio(self.__dao.get_all())

    def mostra_tela(self):

        funcoes = {
            1: self.relatorio_combates,
        }

        super(ControladorRelatorio, self).mostra_tela(funcoes)
