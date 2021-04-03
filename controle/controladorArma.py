from controle.controladorGenerico import ControladorGenerico
from limite.telaArma import TelaArma
from entidade.arma import Arma


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
        self.tela.executado_com_sucesso()

    def pega_arma_por_id(self):
        if self.__armas:
            valores_validos = [arma.id for arma in self.__armas]
            id = self.tela.pega_id(valores_validos)
            for arma in self.__armas:
                if arma.id == id:
                    return arma
        else:
            self.tela.lista_armas_vazia()
            return None

    def remove_arma(self):
        arma = self.pega_arma_por_id()
        try:
            remover = self.tela.confirma_remocao(arma.nome)
        except AttributeError:
            pass
        else:
            if remover:
                self.__armas.remove(arma)
                self.tela.arma_removida_com_sucesso(arma.nome)

    def mostra_atributos_da_arma(self, arma=None):
        if not arma:
            arma = self.pega_arma_por_id()
        try:
            self.tela.mostra_atributos_da_arma(arma)
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
        }

        super(ControladorArma, self).mostra_tela(funcoes)
