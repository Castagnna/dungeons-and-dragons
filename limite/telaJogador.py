from limite.telaGenerica import TelaGenerica


class TelaJogador(TelaGenerica):

    def __init__(self, controlador):
        super(TelaJogador, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU JOGADOR"

        opcoes = (
            (1, "Novo jogador"),
            (2, "Listar jogadores"),
            (3, "Excluir jogador"),
            (4, "Mostrar atributos do jogador"),
            (5, "Alterar atributos do jogador"),
            (6, "Equipar arma no jogador"),
            (7, "Desequipar arma do jogador"),
            (8, "Mostrar armas do jogador"),
            (9, "Atacar Monstro"),
            (10, "Lancar magia"),
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

    def pega_dados_do_jogador(self) -> dict:
        return {
            "nome": self.pega_dado("Nome: ", "str"),
            "forca": self.pega_dado("Forca: ", "int"),
            "destreza": self.pega_dado("Destreza: ", "int"),
            "constituicao": self.pega_dado("Constituicao: ", "int"),
            "inteligencia": self.pega_dado("Inteligencia: ", "int"),
            "sabedoria": self.pega_dado("Sabedoria: ", "int"),
            "carisma": self.pega_dado("Carisma: ", "int"),
            "imagem": self.pega_imagem('personagens/'),
            "ca": self.pega_dado("Ca: ", "int"),
            "vida_maxima": self.pega_dado("Vida maxima: ", "int"),
            "vida_atual": self.pega_dado("Vida atual: ", "int"),
            "tamanho": self.pega_dado("Tamanho: ", "str",['Minusculo', 'Pequeno', 'Medio', 'Grande', 'Enorme', 'Colossal']),
            "nome_jogador": self.pega_dado("Nome do jogador: ", "str"),
            "level": self.pega_dado("Level: ", "int"),
            "experiencia": self.pega_dado("Experiencia: ", "int"),
        }

    @staticmethod
    def mostra_jogadores(jogadores: list):
        print("\n------ Lista de jogadores cadastrados ------")
        for jogador in jogadores:
            print("{} | {}".format(jogador.id, jogador.nome))

    def lista_jogadores_vazia(self):
        self.monstra_mensagem("A lista de jogadores esta vazia")

    def confirma_remocao(self, nome: str):
        return self.tela_confirma("Remover >> {} << ?".format(nome))

    def jogador_removido_com_sucesso(self, nome: str):
        self.monstra_mensagem("Jogador {} excluido com sucesso".format(nome))

    @staticmethod
    def mostra_arma_do_jogador(
        id: int,
        nome: str,
        quantidade_dado: int,
        numero_faces: int,
        mostra_titulo: bool = True,
    ):
        if mostra_titulo:
            print("\n----- Armas do Jogador -----")
        print(f"id: {id}, nome: {nome}, dados: {quantidade_dado}, faces: {numero_faces}")

    def pega_dano(self):
        return self.pega_dado("Insira o valor de dano: ", "int", None, True)

    def resumo_combate(self, atacante: str, defensor: str, dano: int):
        mensagem = f"{atacante} causou {dano} ao {defensor}"
        self.monstra_mensagem(mensagem)
