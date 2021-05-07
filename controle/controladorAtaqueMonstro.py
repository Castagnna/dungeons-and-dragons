from dao.ataqueDAO import AtaqueDAO
from dao.ataqueContadorDAO import AtaqueContadorDAO

from controle.controladorGenerico import ControladorGenerico

from entidade.ataqueMonstro import AtaqueMonstro

from limite.telaAtaqueMonstro import TelaAtaqueMonstro
from limite.telaAtaqueNovo import TelaAtaqueNovo
from limite.telaAtaqueLista import TelaAtaqueLista
from limite.telaAtaqueRemove import TelaAtaqueRemove
from limite.telaAtaquePega import TelaAtaquePega


class ControladorAtaqueMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorAtaqueMonstro, self).__init__(TelaAtaqueMonstro(self))
        self.__tela_ataque_novo = TelaAtaqueNovo(self)
        self.__tela_ataque_lista = TelaAtaqueLista(self)
        self.__tela_ataque_pega = TelaAtaquePega(self)
        self.__tela_ataque_remove = TelaAtaqueRemove(self)
        self.__controlador_principal = controlador_principal
        self.__dao = AtaqueDAO()
        self.__dao_contador = AtaqueContadorDAO()

    def mostra_tela(self):
        funcoes = {
            1: self.cria_novo_ataque,
            2: self.mostra_ataques,
            3: self.remove_ataque,
            5: self.altera_atributos_ataque_monstro,
            6: self.cria_ataque_teste,
        }

        super(ControladorAtaqueMonstro, self).mostra_tela(funcoes)

    def cria_novo_ataque(self, evento="CONFIRMAR", valores: dict=None):
        if not valores:
            evento, valores = self.__tela_ataque_novo.mostra_tela()

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

        if evento == "CONFIRMAR":
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

            print(evento, valores)

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

    def altera_atributos_ataque_monstro(self):
        ataque = self.pega_ataque_por_id()
        opcao = self.tela.mostra_alterar_ataque()

        funcoes = {
            1: ("nome", "str"),
            2: ("dados", "int"),
            3: ("faces", "int"),
            4: ('dano_bonus', 'int'),
            5: ('acerto', 'int'),
            6: ('cd', 'int'),
            7: ('teste', 'str')
        }

        tipo = funcoes[opcao][1]

        novo_valor = self.tela.pega_dado(
            mensagem="Entre novo valor para {}: ".format(funcoes[opcao][0]),
            tipo=tipo
        )
        if opcao == 1:
            ataque.nome = novo_valor
        elif opcao == 2:
            ataque.quantidade_dado = novo_valor
        elif opcao == 3:
            ataque.numero_faces = novo_valor
        elif opcao == 4:
            ataque.dano_bonus = novo_valor
        elif opcao == 5:
            ataque.acerto = novo_valor
        elif opcao == 6:
            ataque.cd = novo_valor
        else:
            ataque.teste = novo_valor
