
from entidade.arma import Arma

from dao.armaDAO import ArmaDAO
from dao.armaContadorDAO import ArmaContadorDAO

from limite.telaArma import TelaArma
from limite.telaArmaNova import TelaArmaNova
from limite.telaArmaLista import TelaArmaLista
from limite.telaArmaRemove import TelaArmaRemove
from limite.telaArmaAltera import TelaArmaAltera
from limite.telaArmaPega import TelaArmaPega


class ControladorArma:
    def __init__(self, controlador_principal):
        self.__tela_arma = TelaArma(self)
        self.__tela_arma_nova = TelaArmaNova(self)
        self.__tela_arma_lista = TelaArmaLista(self)
        self.__tela_arma_remove = TelaArmaRemove(self)
        self.__tela_arma_altera = TelaArmaAltera(self)
        self.__tela_arma_pega = TelaArmaPega(self)
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

        if evento == "CONFIRMAR":

            arma = Arma(
                id=self.__dao_contador.get() + 1,
                nome=valores["NOME"],
                quantidade_dado=int(valores["DADOS"]),
                numero_faces=int(valores["FACES"]),
            )
            
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

        lista_ordenada_de_armas = self.ordena_valores_do_dicionario_por_chave(self.__dao.get_dao())

        mostra_tela = True

        while mostra_tela:

            evento, valores = self.__tela_arma_pega.mostra_tela(lista_ordenada_de_armas)

            if evento == "CONFIRMA":
                try:
                    id = int(valores["ID"])
                    arma = self.__dao.get(id)
                    mostra_tela = False
                    self.__tela_arma_pega.fecha_tela()
                    return arma
                except ValueError:
                    self.__tela_arma_pega.popup_falha(mensagem="O valor precisa ser inteiro")
                    self.__tela_arma_pega.fecha_tela()
                except KeyError:
                    self.__tela_arma_pega.popup_falha(mensagem="Arma não encontrada")
                    self.__tela_arma_pega.fecha_tela()
            elif evento == "CANCELA" or evento == None:
                mostra_tela = False
                self.__tela_arma_pega.fecha_tela()
        return None

    def remove_arma(self):

        arma = self.pega_arma_por_id()

        if not arma:
            return

        try:
            self.__dao.remove(arma)
            self.__tela_arma_remove.popup_sucesso()
            self.__tela_arma_remove.fecha_tela()
        except KeyError:
            self.__tela_arma_remove.popup_falha(mensagem="Arma não encontrada")
            self.__tela_arma_remove.fecha_tela()

    def alterar_arma(self):

        arma = self.pega_arma_por_id()

        if not isinstance(arma, Arma):
            self.__tela_arma_altera.fecha_tela()
            return

        dados = {
            "ID": arma.id,
            "NOME": arma.nome,
            "DADOS": arma.quantidade_dado,
            "FACES": arma.numero_faces,
        }

        evento, valores = self.__tela_arma_altera.mostra_tela(dados)
    
        if evento == "CONFIRMA":
            arma.nome = valores["NOME"]
            arma.quantidade_dado = int(valores["DADOS"])
            arma.numero_faces = int(valores["FACES"])
            self.__tela_arma_altera.popup_sucesso()

        self.__tela_arma_altera.fecha_tela()

    def mostra_tela(self):

        evento, _ = self.__tela_arma.mostra_tela()

        if evento == "VOLTAR":
            self.__tela_arma.fecha_tela()
            self.__controlador_principal.mostra_tela()

        telas = {
            "NOVA_ARMA": self.cria_nova_arma,
            "LISTA_ARMAS": self.mostra_armas,
            "REMOVE_ARMA": self.remove_arma,
            "ARTERA_ARMA": self.alterar_arma,
            "ARMA_TESTE": self.cria_arma_teste,
        }

        try:
            self.__tela_arma.fecha_tela()
            telas[evento]()
            self.mostra_tela()
        except KeyError:
            pass




        
