from controle.controladorGenerico import ControladorGenerico

from limite.relatorio.telaRelatorio import TelaRelatorio
from limite.relatorio.telaRelatorioCombate import TelaRelatorioCombate

from dao.combateContadorDAO import CombateContadorDAO
from dao.combateDAO import CombateDAO


class ControladorRelatorio:
    def __init__(self, controlador_principal):
        self.__tela_relatorio = TelaRelatorio(self)
        self.__tela_combate = TelaRelatorioCombate(self)
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

    @staticmethod
    def ordena_valores_do_dicionario_por_chave(dicionario: dict):
        lista_ordenada = []
        for key in sorted(dicionario.keys()):
            lista_ordenada.append(dicionario[key])
        return lista_ordenada

    def relatorio_combates(self):

        combates_ordenados = self.ordena_valores_do_dicionario_por_chave(self.__dao.get_dao())

        self.__tela_combate.mostra_tela(combates_ordenados)
        self.__tela_combate.fecha_tela()

    def mostra_tela(self):

        evento, _ = self.__tela_relatorio.mostra_tela()

        if evento == "VOLTAR":
            self.__tela_relatorio.fecha_tela()
            self.__controlador_principal.mostra_tela()

        telas = {
            "COMBATE": self.relatorio_combates,
        }

        try:
            self.__tela_relatorio.fecha_tela()
            telas[evento]()
            self.mostra_tela()
        except KeyError:
            pass
