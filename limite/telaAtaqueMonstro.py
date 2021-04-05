from limite.telaGenerica import TelaGenerica


class TelaAtaqueMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaAtaqueMonstro, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU ATAQUE MONSTRO"

        opcoes = (
            (1, "Novo ataque"),
            (2, "Ataques cadastrados"),
            (3, "Remove ataque"),
            (4, "Mostra atributos do ataque"),
            (5, "Alterar ataque"),
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

    def pega_dados_de_ataque(self) -> dict:
        return {
            "nome": self.pega_dado("Nome: ", "str"),
            "quantidade_dado": self.pega_dado("Quantidade de dados: ", "int"),
            "numero_faces": self.pega_dado("Numero de faces do dado: ", "int"),
            "dano_bonus": self.pega_dado("Dano bonus: ", "int"),
            "acerto": self.pega_dado("Acerto: ", "int"),
            "cd": self.pega_dado("Cd: ", "int"),
            "teste": self.pega_dado("Teste: ", "str", ["Forca", "Destreza", "Constituicao", "Sabedoria", "Inteligencia", "Carisma", "Nenhum"]),
        }

    @staticmethod
    def mostra_ataques(ataques: list):
        print("\n------ Lista de armas cadastradas ------")
        for ataque in ataques:
            print("{} | {}".format(ataque.id, ataque.nome))

    @staticmethod
    def mostra_atributos_do_ataque(ataque):
        print("\n------ Atributos de {} ------".format(ataque.nome))
        print("Id: {}".format(ataque.id))
        print("Nome: {}".format(ataque.nome))
        print("Quantidade dado: {}".format(ataque.quantidade_dado))
        print("Numero de faces: {}".format(ataque.numero_faces))
        print("Dados bonus: {}".format(ataque.dados_bonus))
        print("Acerto: {}".format(ataque.acerto))
        print("Cd: {}".format(ataque.cd))
        print("Teste: {}".format(ataque.teste))

    def mostra_alterar_ataque(self) -> int:
        titulo_da_tela = "ALTERAR ATAQUE MONSTRO"

        opcoes = (
            (1, "Novo nome"),
            (2, "Alterar quantidade de dados"),
            (3, "Alterar faces"),
            (4, "Dados bonus"),
            (5, "Acerto"),
            (6, "Cd"),
            (7, "Teste"),
        )

        self.cria_menu_opcoes(titulo_da_tela, opcoes)

        opcao = self.pega_dado(
            mensagem="\n>>> Escolha uma opção: ",
            tipo="int",
            valores_validos=[codigo for codigo, _ in opcoes],
            confirmar=False
        )

        return opcao

    def pega_id_ataque(self, valores_validos) -> int:
        print("Ataque Monstro, ", end="")
        return self.pega_id(valores_validos)

    def lista_ataques_monstro_vazia(self):
        self.monstra_mensagem("A lista de ataques de monstros esta vazia")