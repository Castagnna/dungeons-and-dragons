#controladores
from controle.controladorGenerico import ControladorGenerico

# telas
from limite.telaArmaPrincipal import TelaArmaPrincipal
from limite.telaArmaNova import TelaArmaNova
from limite.telaArmaLista import TelaArmaLista

# entidades
from entidade.arma import Arma


class ControladorArma:
    __instace = None

    def __init__(self, controlador_principal=None):
        # super(ControladorArma, self).__init__(TelaArma(self))
        self.__controlador_principal = controlador_principal
        self.__armas = {}
        self.__counta_armas = 1
        self.__tela_arma_principal = TelaArmaPrincipal(self)
        self.__tela_arma_nova = TelaArmaNova(self)
        self.__tela_arma_lista = TelaArmaLista(self)

    def __new__(cls, controlador_principal):
        if ControladorArma.__instace is None:
            ControladorArma.__instace = object.__new__(cls)
        return ControladorArma.__instace

    """
    getters
    """

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def armas(self):
        return self.__armas

    """
    methods
    """

    def mostra_tela_principal(self):

        funcoes = {
            "NOVA_ARMA": self.cria_nova_arma,
            "LISTA_ARMAS": self.lista_armas,
        }

        evento, _ = self.__tela_arma_principal.mostra_tela()

        funcoes[evento]()
        
    def cria_nova_arma(self, dados = None):

        if not dados:
            evento, valores = self.__tela_arma_nova.mostra_tela()
        
        if evento == "CONFIRMAR":

            arma = Arma(
                id=self.__counta_armas,
                nome=valores["NOME"],
                quantidade_dado=valores["DADOS"],
                numero_faces=valores["FACES"],
            )

            self.__armas[arma.id] = arma
            self.__counta_armas += 1
            self.__tela_arma_nova.popup_sucesso()

        self.__tela_arma_nova.fecha_tela()

    def lista_armas(self):
        self.__tela_arma_lista.mostra_tela()
        self.__tela_arma_lista.fecha_tela()

    # def cria_arma_teste(self):
    #     dados = {
    #         "nome": f"arma {self.__counta_armas}",
    #         "quantidade_dado": 1,
    #         "numero_faces": 6,
    #     }
    #     self.cria_nova_arma(dados)

    # def pega_arma_por_id(self):
    #     if self.__armas:
    #         valores_validos = [arma.id for arma in self.__armas]
    #         id = self.tela.pega_id(valores_validos)
    #         for arma in self.__armas:
    #             if arma.id == id:
    #                 return arma
    #     else:
    #         self.tela.lista_armas_vazia()
    #         return None

    # def remove_arma(self):
    #     arma = self.pega_arma_por_id()
    #     try:
    #         remover = self.tela.confirma_remocao(arma.nome)
    #     except AttributeError:
    #         pass
    #     else:
    #         if remover:
    #             self.__armas.remove(arma)
    #             self.tela.arma_removida_com_sucesso(arma.nome)

    # def mostra_atributos_da_arma(self, arma: Arma = None):
    #     if not arma:
    #         arma = self.pega_arma_por_id()
    #     try:
    #         atributos = {
    #             "id": arma.id,
    #             "nome": arma.nome,
    #             "dados": arma.quantidade_dado,
    #             "faces": arma.numero_faces,
    #         }
    #         self.tela.mostra_atributos_da_arma(atributos)
    #     except AttributeError:
    #         pass

    # def alterar_arma(self):
    #     arma = self.pega_arma_por_id()
    #     opcao = self.tela.mostra_alterar_arma()

    #     funcoes = {
    #         1: ("nome", "str"),
    #         2: ("dados", "int"),
    #         3: ("faces", "int"),
    #     }

    #     tipo = funcoes[opcao][1]

    #     novo_valor = self.tela.pega_dado(
    #         mensagem="Entre novo valor para {}: ".format(funcoes[opcao][0]),
    #         tipo=tipo
    #     )
    #     if opcao == 1:
    #         arma.nome = novo_valor
    #     elif opcao == 2:
    #         arma.quantidade_dado = novo_valor
    #     else:
    #         arma.numero_faces = novo_valor

    # def mostra_tela(self):

    #     funcoes = {
    #         1: self.cria_nova_arma,
    #         2: self.mostra_armas,
    #         3: self.remove_arma,
    #         4: self.mostra_atributos_da_arma,
    #         5: self.alterar_arma,
    #         77: self.cria_arma_teste,
    #     }

    #     super(ControladorArma, self).mostra_tela(funcoes)
