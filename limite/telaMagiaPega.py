from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaMagiaPega(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_de_magias = []
        self.init_components()

    def monta_lista_str(self, lista_de_magias: list):
        def monta_string(id, nome):
            return f'{id:^4} | {nome:^10}'

        lista_str = ['Id | Nome']

        for magia in lista_de_magias:
            string = monta_string(
                magia.id,
                magia.nome
            )
            lista_str.append(string)

        return lista_str

    def init_components(self, **kwargs):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__lista_de_magias)

        layout = [
            [sg.Listbox(values=valores, size=(30, 6))],
            [sg.Text('Seleciona a magia por id:'), sg.InputText('', key='ID')],
            [sg.Submit('Confirma', key='CONFIRMA')],
            [sg.Cancel('Cancela', key='CANCELA')]
        ]

        janela = sg.Window("Escolha de arma", default_element_size=(40, 10)).Layout(layout)
        super(TelaMagiaPega, self).cria_janela(janela)

    def mostra_tela(self, lista_de_magias):
        self.__lista_de_magias = lista_de_magias
        return super().mostra_tela()