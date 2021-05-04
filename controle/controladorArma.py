from controle.controladorGenerico import ControladorGenerico
from limite.telaArma import TelaArma
from entidade.arma import Arma
from dao.armaDAO import ArmaDAO
from dao.armaContadorDAO import ArmaContadorDAO
from limite.telaArmaNova import TelaArmaNova
from limite.telaArmaLista import TelaArmaLista


class ControladorArma(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorArma, self).__init__(TelaArma(self))
        self.__tela_arma_nova = TelaArmaNova(self)
        self.__tela_arma_lista = TelaArmaLista(self)
        self.__controlador_principal = controlador_principal
        self.__dao = ArmaDAO()
        self.__dao_contador = ArmaContadorDAO()

    @property
    def controlador_principal(self):
        return self.__controlador_principal

    @property
    def armas(self):
        return self.__dao.get_all()

    """
    Methods
    """

    def cria_nova_arma(self, evento="CONFIRMAR", valores: dict=None):
        if not valores:
            evento, valores = self.__tela_arma_nova.mostra_tela()

        arma = Arma(
            id=self.__dao_contador.get() + 1,
            nome=valores["NOME"],
            quantidade_dado=int(valores["DADOS"]),
            numero_faces=int(valores["FACES"]),
        )

        if evento == "CONFIRMAR":
            self.__dao.add(arma)
            self.__dao_contador.add(1)
            self.__tela_arma_nova.popup_sucesso()

        self.__tela_arma_nova.fecha_tela()

    def cria_arma_teste(self):
        valores = {
            "NOME": f"arma {self.__dao_contador.get() + 1}",
            "DADOS": 1,
            "FACES": 6,
        }
        self.cria_nova_arma(valores=valores)

    @staticmethod
    def ordena_valores_do_dicionario_por_chave(dicionario: dict):
        lista_ordenada = []
        for key in sorted(dicionario.keys()):
            lista_ordenada.append(dicionario[key])
        return lista_ordenada

    def mostra_armas(self):

        lista_ordenada_de_armas = self.ordena_valores_do_dicionario_por_chave(self.__dao.get_dao())

        evento, _ = self.__tela_arma_lista.mostra_tela(lista_ordenada_de_armas)
        if evento == "OK":
            self.__tela_arma_lista.fecha_tela()

    def pega_arma_por_id(self):
        if self.__dao.get_all():
            valores_validos = [arma.id for arma in self.__dao.get_all()]
            id = self.tela.pega_id(valores_validos)
            return self.__dao.get(id)
        else:
            self.tela.lista_armas_vazia()
            return None

    def remove_arma(self):
        arma = self.pega_arma_por_id()
        try:
            self.__dao.remove(arma)
            self.tela.arma_removida_com_sucesso(arma.nome)
        except AttributeError:
            pass
            
    def mostra_atributos_da_arma(self, arma: Arma = None):
        if not arma:
            arma = self.pega_arma_por_id()
        try:
            atributos = {
                "id": arma.id,
                "nome": arma.nome,
                "dados": arma.quantidade_dado,
                "faces": arma.numero_faces,
            }
            self.tela.mostra_atributos_da_arma(atributos)
        except AttributeError:
            pass

    def alterar_arma(self):
        arma = self.pega_arma_por_id()
        opcao = self.tela.mostra_alterar_arma()

        funcoes = {
            1: ("nome", "str"),
            2: ("dados", "int"),
            3: ("faces", "int"),
        }

        tipo = funcoes[opcao][1]

        novo_valor = self.tela.pega_dado(
            mensagem="Entre novo valor para {}: ".format(funcoes[opcao][0]),
            tipo=tipo
        )
        if opcao == 1:
            arma.nome = novo_valor
        elif opcao == 2:
            arma.quantidade_dado = novo_valor
        else:
            arma.numero_faces = novo_valor

    def mostra_tela(self):

        funcoes = {
            1: self.cria_nova_arma,
            2: self.mostra_armas,
            3: self.remove_arma,
            4: self.mostra_atributos_da_arma,
            5: self.alterar_arma,
            77: self.cria_arma_teste,
        }

        super(ControladorArma, self).mostra_tela(funcoes)
