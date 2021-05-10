from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg


class TelaMonstroPega(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_de_monstro = []
        self.init_components()

    def monta_lista_str(self, lista_de_monstro: list):
        def monta_string(id, nome):
            return f"{id:^4}|{nome:^10}"

        lista_str = ['Id | Nome']

        for monstro in lista_de_monstro:
            string = monta_string(monstro.id,
                                  monstro.nome
                                  )
            lista_str.append(string)

        return lista_str

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__lista_de_monstro)

        layout = [
            [sg.Listbox(values=valores, size=(30,6))],
            [sg.Text('Selecione o monstro por id'), sg.InputText('', key='ID')],
            [sg.Submit('Confirma', key='CONFIRMAR')],
            [sg.Cancel('Cancela', key='CANCELA')]
        ]

        janela = sg.Window('Escolha de jogador', default_element_size=(40,10)).Layout(layout)
        super(TelaMonstroPega, self).cria_janela(janela)

    def mostra_tela(self, lista_de_monstro):
        self.__lista_de_monstro = lista_de_monstro
        return super().mostra_tela()