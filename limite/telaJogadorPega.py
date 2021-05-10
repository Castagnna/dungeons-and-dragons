from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg


class TelaJogadorPega(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_de_jogadores = []
        self.init_components()

    def monta_lista_str(self, lista_de_jogadores: list):
        def monta_string(id, nome):
            return f"{id:^4}|{nome:^10}"

        lista_str = ['Id | Nome']

        for jogador in lista_de_jogadores:
            string = monta_string(jogador.id,
                                  jogador.nome
                                  )
            lista_str.append(string)

        return lista_str

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__lista_de_jogadores)

        layout = [
            [sg.Listbox(values=valores, size=(30,6))],
            [sg.Text('Selecione o jogador por id'), sg.InputText('', key='ID')],
            [sg.Submit('Confirma', key='CONFIRMAR')],
            [sg.Cancel('Cancela', key='CANCELA')]
        ]

        janela = sg.Window('Escolha de jogador', default_element_size=(40,10)).Layout(layout)
        super(TelaJogadorPega, self).cria_janela(janela)

    def mostra_tela(self, lista_de_jogadores):
        self.__lista_de_jogadores = lista_de_jogadores
        return super().mostra_tela()
