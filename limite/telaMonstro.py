from limite.telaGenerica import TelaGenerica


class TelaMonstro(TelaGenerica):

    def __init__(self, controlador):
        super(TelaMonstro, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU MONSTRO"

        opcoes = (
            (1, "Novo monstro"),
            (2, "Listar monstros"),
            (3, "Excluir Monstro"),
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

    def pega_dados_do_monstro(self) -> dict:
        return {
            # TODO: implementar
        }
    
    @staticmethod
    def mostra_monstros(monstros: list):
        print("\n------ Lista de monstros cadastrados ------\n")
        for monstro in monstros:
            print(f"{monstro.id} | {monstro.nome}")

    def lista_monstros_vazia(self):
        self.monstra_mensagem("A lista de monstros esta vazia")

    def confirma_remocao(self, nome: str):
        return self.tela_confirma("Remover >> {} << ?".format(nome))

    def monstro_removido_com_sucesso(self, nome: str):
        self.monstra_mensagem("Monstro {} excluido com sucesso".format(nome))
