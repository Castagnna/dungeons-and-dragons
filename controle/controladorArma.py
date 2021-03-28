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
        self.tela.mostra_armas(self.__armas)

    def cria_nova_arma(self):
        dados = self.tela.pega_dados_da_arma()
        arma = Arma(
            id=self.__counta_armas,
            **dados
        )
        self.__armas.append(arma)
        self.__counta_armas += 1
        self.tela.monstra_mensagem("Arma {} criado com sucesso".format(arma.nome))

    def pega_arma_por_id(self):
        if self.__armas:
            valores_validos = [arma.id for arma in self.__armas]
            id = self.tela.pega_dado("Id da arma: ", "int", valores_validos, False)
            for arma in self.__armas:
                if arma.id == id:
                    return arma
        else:
            self.tela.monstra_mensagem("A lista de arma esta vazia")
            return None

    def remove_arma(self):
        arma = self.pega_arma_por_id()
        try:
            self.tela.tela_confirma("Remover >> {} << ?".format(arma.nome))
        except AttributeError:
            pass
        else:
            self.__armas.remove(arma)
            self.tela.monstra_mensagem("Arma {} excluida com sucesso".format(arma.nome))

    def mostra_atributos_da_arma(self, arma=None):
        if not arma:
            arma = self.pega_arma_por_id()
        try:
            self.tela.mostra_atributos_da_arma(arma)
        except AttributeError:
            pass

    def alterar_arma(self):
        arma = self.pega_arma_por_id()
        self.mostra_atributos_da_arma(arma)

        atributos = {
            "nome": ("nome", "str"),
            "dados": ("quantidade_dado", "int"),
            "faces": ("numero_faces", "int"),
        }

        opcao = self.tela.pega_dado(
            mensagem="Entre o nome do atributo para alterar: ",
            tipo="str",
            valores_validos=list(atributos.keys()),
            confirmar=False
        )

        tipo = atributos[opcao][1]
        novo_valor = self.tela.pega_dado(
            mensagem="Entre novo valor para {}: ".format(opcao),
            tipo=tipo
        )

        atributo = atributos[opcao][0]
        atributo = Arma.__dict__[atributo]
        atributo.__set__(arma, novo_valor)

        self.mostra_atributos_da_arma(arma)

    def mostra_tela(self):

        funcoes = {
            1: self.cria_nova_arma,
            2: self.mostra_armas,
            3: self.remove_arma,
            4: self.mostra_atributos_da_arma,
            5: self.alterar_arma,
            88: self.controlador_principal.mostra_tela,
        }

        super(ControladorArma, self).mostra_tela(funcoes)
