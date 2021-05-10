from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaPersonagemLista(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_de_personagens = []
        self.init_components()

    def monta_lista_str(self, lista_de_personagens: list):

        def monta_string(id, nome):
            return f'{id:^4} | {nome:^10}'

        lista_str = [' Id | Nome']

        for personagem in lista_de_personagens:
            string = monta_string(
                personagem.id,
                personagem.nome
            )
            lista_str.append(string)

        return lista_str

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__lista_de_personagens)

        layout = [
            [sg.Listbox(values=valores, size=(30, 6))],
            [sg.Cancel('OK', key='OK')]
        ]

        janela = sg.Window('Lista de Personagens', default_element_size=(40,10)).Layout(layout)
        super(TelaPersonagemLista, self).cria_janela(janela)

    def mostra_tela(self, lista_de_personagens):
        self.__lista_de_personagens = lista_de_personagens
        return super().mostra_tela()