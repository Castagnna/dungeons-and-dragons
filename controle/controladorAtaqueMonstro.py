from dao.ataqueDAO import AtaqueDAO
from dao.ataqueContadorDAO import AtaqueContadorDAO

from controle.controladorGenerico import ControladorGenerico

from entidade.ataqueMonstro import AtaqueMonstro

from limite.telaAtaqueMonstro import TelaAtaqueMonstro
from limite.telaAtaqueNovo import TelaAtaqueNovo


class ControladorAtaqueMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorAtaqueMonstro, self).__init__(TelaAtaqueMonstro(self))
        self.__ataque_novo = TelaAtaqueNovo(self)
        self.__controlador_principal = controlador_principal
        self.__dao = AtaqueDAO()
        self.__dao_contador = AtaqueContadorDAO()

    def mostra_tela(self):
        funcoes = {
            1: self.cria_novo_ataque_monstro,
            2: self.mostra_ataques_monstro,
            3: self.remove_ataque_monstro,
            4: self.mostra_atributos_ataque_monstro,
            5: self.altera_atributos_ataque_monstro
        }

        super(ControladorAtaqueMonstro, self).mostra_tela(funcoes)

    def cria_novo_ataque_monstro(self):
        dados = self.tela.pega_dados_de_ataque()
        novo_ataque = AtaqueMonstro(
            id=self.__dao_contador.get() + 1,
            **dados
        )
        self.__dao.add(novo_ataque)
        self.__dao_contador.add(1)
        
        self.tela.executado_com_sucesso()

    def mostra_ataques_monstro(self):
        self.tela.mostra_ataques(self.__dao.get_all())

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
