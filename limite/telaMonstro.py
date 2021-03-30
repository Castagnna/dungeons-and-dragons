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
            print("{} | {}".format(monstro.codigo, monstro.nome))
