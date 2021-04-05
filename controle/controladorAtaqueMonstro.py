from controle.controladorGenerico import ControladorGenerico
from limite.telaAtaqueMonstro import TelaAtaqueMonstro
from entidade.ataqueMonstro import AtaqueMonstro


class ControladorAtaqueMonstro(ControladorGenerico):
    def __init__(self, controlador_principal):
        super(ControladorAtaqueMonstro, self).__init__(TelaAtaqueMonstro(self))
        self.__controlador_principal = controlador_principal
        self.__ataques_monstro = []
        self.__controlador_principal = controlador_principal
        self.__counta_ataque_monstro = 0

    def mostra_tela(self, funcoes: dict):
        funcoes = {
            1: self.cria_novo_ataque_monstro,
            2: self.mostra_ataques_monstro,
            3: self.remove_ataque_monstro,
            4: self.mostra_atributos_ataque_monstro,
            5: self.altera_atributos_ataque_monstro
        }

        super(ControladorAtaqueMonstro, self).mostra_tela(funcoes)

    def cria_novo_ataque_monstro(self):
        dados = self.__tela.pega_dados_de_ataque()
        novo_ataque = AtaqueMonstro(
            id=self.__counta_ataque_monstro,
            **dados
        )
        self.__counta_ataque_monstro += 1
        self.__ataques_monstro.append(novo_ataque)
        self.tela.executado_com_sucesso()

    def mostra_ataques_monstro(self):
        self.tela.mostra_ataques(self.__ataques_monstro)

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
        pass

    def pega_ataque_por_id(self) -> AtaqueMonstro:
        if self.__ataques_monstro:
            valores_validos = [ataque.id for ataque in self.__ataques_monstro]
            id = self.tela.pega_id_ataque(valores_validos)
            for ataque in self.__ataques_monstro:
                if ataque.id == id:
                    return ataque
        else:
            self.tela.lista_ataques_monstro_vazia()
            return None