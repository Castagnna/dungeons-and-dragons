from limite.telaGenerica import TelaGenerica


class TelaMagia(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMagia, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU MAGIA"

        opcoes = (
            (1, "Nova magia"),
            # (2, "Mostra atributos da magia"),
            # (3, "Alterar magia"),
            (88, "Voltar"),
            (99, "Finaliza programa")
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return self.protege_finalizar(opcao)
    
    def pega_dados_da_magia(self) -> dict:
        return {
            "nome": self.pega_dado("Nome: ", "str"),
            "quantidade_dado": self.pega_dado("Quantidade de dados: ", "int"),
            "numero_faces": self.pega_dado("Numero de faces do dado: ", "int"),
            "circulo": self.pega_dado("Circulo: ", "int"),
            "teste": self.pega_dado("Teste: ", "str"),
        }

    @staticmethod
    def mostra_magias(magias: list):
        print("\n------ Lista de magias castradas ------")
        for magia in magias:
            print("{} | {}".format(magia.id, magias.nome))

    @staticmethod
    def mostra_atributos_da_magia(magia):
        print("\n------ Atributos de {} ------".format(magia.nome))
        print("Id: {}".format(magia.id))
        print("Nome: {}".format(magia.nome))
        print("Quantidade dado: {}".format(magia.quantidade_dado))
        print("Numero de faces: {}".format(magia.numero_faces))
        print("Circulo: {}".format(magia.circulo))
        print("Teste: {}".format(magia.teste))

    def mostra_alterar_arma(self) -> int:
        titulo_da_tela = "ALTERAR MAGIA"

        opcoes = (
            (1, "Novo nome"),
            (2, "Alterar quantidade de dados"),
            (3, "Alterar faces"),
            (4, "Alterar circulo"),
            (5, "Alterar teste"),
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return opcao
