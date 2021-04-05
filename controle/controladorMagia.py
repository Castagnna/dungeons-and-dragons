from controle.controladorGenerico import ControladorGenerico
from limite.telaMagia import TelaMagia
from entidade.magia import Magia


class ControladorMagia(ControladorGenerico):
    def __init__(self, controlador_jogador):
        super(ControladorMagia, self).__init__(TelaMagia(self))
        self.__controlador_jogador = controlador_jogador
        self.__counta_magias = 0

    def cria_magia(self, dados: dict = None) -> Magia:
        if not dados:
            dados = self.tela.pega_dados_da_magia()
        magia = Magia(
            id=self.__counta_magias,
            **dados
        )
        self.__counta_magias += 1
        return magia

    def cria_magia_teste(self) -> Magia:
        dados = {
            "nome": f"bola de fogo {self.__counta_magias}",
            "quantidade_dado": 2,
            "numero_faces": 6,
            "circulo": 1,
            "teste": "sim",
        }
        return self.cria_magia(dados)

    def mostra_tela(self):

        funcoes = {
            (1, self.cria_magia),
            (77, self.cria_magia_teste),
        }

        super(ControladorMagia, self).mostra_tela(funcoes)

    def altera_magia(self, magia):
        opcao = self.tela.mostra_alterar_magia()

        funcoes = {
            1: ("nome", "str"),
            2: ("dados", "int"),
            3: ("faces", "int"),
            4: ('circulo', 'int'),
            5: ('teste', 'str')
        }

        tipo = funcoes[opcao][1]

        novo_valor = self.tela.pega_dado(
            mensagem="Entre novo valor para {}: ".format(funcoes[opcao][0]),
            tipo=tipo
        )
        if opcao == 1:
            magia.nome = novo_valor
        elif opcao == 2:
            magia.quantidade_dado = novo_valor
        elif opcao == 3:
            magia.numero_faces = novo_valor
        elif opcao == 4:
            magia.circulo = novo_valor
        else:
            magia.teste = novo_valor