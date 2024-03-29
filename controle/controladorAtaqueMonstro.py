from dao.ataqueDAO import AtaqueDAO
from dao.ataqueContadorDAO import AtaqueContadorDAO

from entidade.ataqueMonstro import AtaqueMonstro

from limite.ataque.telaAtaque import TelaAtaque
from limite.ataque.telaAtaqueNovo import TelaAtaqueNovo
from limite.ataque.telaAtaqueLista import TelaAtaqueLista
from limite.ataque.telaAtaqueRemove import TelaAtaqueRemove
from limite.ataque.telaAtaquePega import TelaAtaquePega
from limite.ataque.telaAtaqueAltera import TelaAtaqueAltera


class ControladorAtaqueMonstro:
    def __init__(self, controlador_principal):
        self.__tela_ataque = TelaAtaque(self)
        self.__tela_ataque_novo = TelaAtaqueNovo(self)
        self.__tela_ataque_lista = TelaAtaqueLista(self)
        self.__tela_ataque_pega = TelaAtaquePega(self)
        self.__tela_ataque_remove = TelaAtaqueRemove(self)
        self.__tela_ataque_altera = TelaAtaqueAltera(self)
        self.__controlador_principal = controlador_principal
        self.__dao = AtaqueDAO()
        self.__dao_contador = AtaqueContadorDAO()

    def mostra_tela(self):

        evento, _ = self.__tela_ataque.mostra_tela()

        if evento == "VOLTAR" or evento == None:
            self.__tela_ataque.fecha_tela()
            self.__controlador_principal.mostra_tela()

        telas = {
            "NOVO_ATAQUE": self.cria_novo_ataque,
            "LISTA_ATAQUES": self.mostra_ataques,
            "REMOVE_ATAQUE": self.remove_ataque,
            "ARTERA_ATAQUE": self.altera_ataque,
            "ATAQUE_TESTE": self.cria_ataque_teste,
        }

        try:
            self.__tela_ataque.fecha_tela()
            telas[evento]()
            self.mostra_tela()
        except KeyError:
            pass

    def cria_novo_ataque(self, evento="CONFIRMAR", valores: dict=None):
        if not valores:
            evento, valores = self.__tela_ataque_novo.mostra_tela()

        if evento == "CONFIRMAR":
            ataque = AtaqueMonstro(
                id=self.__dao_contador.get() + 1,
                nome=valores["NOME"],
                quantidade_dado=int(valores["DADOS"]),
                numero_faces=int(valores["FACES"]),
                dano_bonus=int(valores["BONUS"]),
                acerto=int(valores["ACERTO"]),
                cd=int(valores["CD"]),
                teste=valores["TESTE"],
            )
            
            self.__dao.add(ataque)
            self.__dao_contador.add(1)
            self.__tela_ataque_novo.popup_sucesso()

        self.__tela_ataque_novo.fecha_tela()

    def cria_ataque_teste(self):
        valores = {
            "NOME": f"ataque {self.__dao_contador.get() + 1}",
            "DADOS": 1,
            "FACES": 1,
            "BONUS": 1,
            "ACERTO": 1,
            "CD": 1,
            "TESTE": "Nenhum"
        }
        self.cria_novo_ataque(valores=valores)

    @staticmethod
    def ordena_valores_do_dicionario_por_chave(dicionario: dict):
        lista_ordenada = []
        for key in sorted(dicionario.keys()):
            lista_ordenada.append(dicionario[key])
        return lista_ordenada

    def mostra_ataques(self):

        lista_ordenada_de_ataques = self.ordena_valores_do_dicionario_por_chave(self.__dao.get_dao())

        evento, _ = self.__tela_ataque_lista.mostra_tela(lista_ordenada_de_ataques)
        if evento == "OK":
            self.__tela_ataque_lista.fecha_tela()

    def pega_ataque_por_id(self):

        lista_ordenada_de_ataques = self.ordena_valores_do_dicionario_por_chave(self.__dao.get_dao())

        mostra_tela = True

        while mostra_tela:

            evento, valores = self.__tela_ataque_pega.mostra_tela(lista_ordenada_de_ataques)

            if evento == "CONFIRMA":
                try:
                    id = int(valores["ID"])
                    ataque = self.__dao.get(id)
                    mostra_tela = False
                    self.__tela_ataque_pega.fecha_tela()
                    return ataque
                except ValueError:
                    self.__tela_ataque_pega.popup_falha(mensagem="O valor precisa ser inteiro")
                    self.__tela_ataque_pega.fecha_tela()
                except KeyError:
                    self.__tela_ataque_pega.popup_falha(mensagem="Ataque não encontrado")
                    self.__tela_ataque_pega.fecha_tela()
            elif evento == "CANCELA" or evento == None:
                mostra_tela = False
                self.__tela_ataque_pega.fecha_tela()
        return None

    def remove_ataque(self):

        ataque = self.pega_ataque_por_id()

        if not ataque:
            return

        try:
            self.__dao.remove(ataque)
            self.__tela_ataque_remove.popup_sucesso()
            self.__tela_ataque_remove.fecha_tela()
        except KeyError:
            self.__tela_ataque_remove.popup_falha(mensagem="Ataque não encontrada")
            self.__tela_ataque_remove.fecha_tela()

    def altera_ataque(self):

        ataque = self.pega_ataque_por_id()

        if not isinstance(ataque, AtaqueMonstro):
            self.__tela_ataque_altera.fecha_tela()
            return

        dados = {
            "ID": ataque.id,
            "NOME": ataque.nome,
            "DADOS": ataque.quantidade_dado,
            "FACES": ataque.numero_faces,
            "BONUS": ataque.dano_bonus,
            "ACERTO": ataque.acerto,
            "CD": ataque.cd,
            "TESTE": ataque.teste,
        }

        evento, valores = self.__tela_ataque_altera.mostra_tela(dados)
    
        if evento == "CONFIRMA":
            ataque.nome = valores["NOME"]
            ataque.quantidade_dado = int(valores["DADOS"])
            ataque.numero_faces = int(valores["FACES"])
            ataque.dano_bonus = int(valores["BONUS"])
            ataque.acerto = int(valores["ACERTO"])
            ataque.cd = int(valores["CD"])
            ataque.teste = valores["TESTE"]
            self.__tela_ataque_altera.popup_sucesso()

        self.__tela_ataque_altera.fecha_tela()
