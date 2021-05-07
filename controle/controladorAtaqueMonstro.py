from dao.ataqueDAO import AtaqueDAO
from dao.ataqueContadorDAO import AtaqueContadorDAO

from controle.controladorGenerico import ControladorGenerico

from entidade.ataqueMonstro import AtaqueMonstro

from limite.telaAtaqueMonstro import TelaAtaqueMonstro
from limite.telaAtaqueNovo import TelaAtaqueNovo
from limite.telaAtaqueLista import TelaAtaqueLista


class ControladorAtaqueMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorAtaqueMonstro, self).__init__(TelaAtaqueMonstro(self))
        self.__tela_ataque_novo = TelaAtaqueNovo(self)
        self.__tela_ataque_lista = TelaAtaqueLista(self)
        self.__controlador_principal = controlador_principal
        self.__dao = AtaqueDAO()
        self.__dao_contador = AtaqueContadorDAO()

    def mostra_tela(self):
        funcoes = {
            1: self.cria_novo_ataque,
            2: self.mostra_ataques,
            3: self.remove_ataque_monstro,
            4: self.mostra_atributos_ataque_monstro,
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

    # def mostra_ataques(self):
    #     self.tela.mostra_ataques(self.__dao.get_all())

    def remove_ataque_monstro(self):
        ataque = self.pega_ataque_por_id()
        try:
            remover = self.tela.confirma_remocao(ataque.nome)
        except AttributeError:
            pass
        else:
            if remover:
                self.__ataques_monstro.remove(ataque)
                self.tela.executado_com_sucesso()

    def mostra_atributos_ataque_monstro(self):
        ataque = self.pega_ataque_por_id()
        if ataque:
            self.tela.mostra_atributos_do_ataque(ataque)

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

    def pega_ataque_por_id(self) -> AtaqueMonstro:
        if self.__dao.get_all():
            valores_validos = [ataque.id for ataque in self.__dao.get_all()]
            id = self.tela.pega_id_ataque(valores_validos)
            return self.__dao.get(id)
        else:
            self.tela.lista_ataques_monstro_vazia()
            return None
