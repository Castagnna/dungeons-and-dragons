from limite.telaGenerica import TelaGenerica


class TelaRelatorio(TelaGenerica):

    def __init__(self, controlador):
        super(TelaRelatorio, self).__init__(controlador)

    def mostra_opcoes(self) -> int:
        titulo_da_tela = "MENU RELATORIOS"

        opcoes = (
            (1, "Relatorio combate"),
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

    @staticmethod
    def cria_relatorio(eventos_combate: list):
        print("evento | atacate | defensor | dano\n")
        for combate in eventos_combate:
            evento = combate['id']
            atacante = combate['atacante']
            defensor = combate['defensor']
            dano = combate['dano']
            print(f"{evento} | {atacante.nome} | {defensor.nome} | {dano}")
