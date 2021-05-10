from limite.telaGenerica import TelaGenerica

import PySimpleGUI as sg

class TelaJogadorArmas(TelaGenerica):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__janela = None
        self.__armas = []
        self.init_components()

    @staticmethod
    def monta_lista_str(lista_de_armas: list):

        def monta_string(id, nome):
            return f"{id:^4}|{nome:^10}"

        lista_str = [" Id |   Nome   | Dados | Faces"]

        for arma in lista_de_armas:
            string = monta_string(
                arma.id,
                arma.nome,
            )
            lista_str.append(string)

        return lista_str

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__armas)

        layout = [
            [sg.Listbox(values=valores, size=(30, 6))],
            [sg.Text("Seleciona a arma por id:"), sg.InputText("", key="ID")],
            [sg.Submit("Confirma", key="CONFIRMA")],
            [sg.Cancel("Cancela", key="CANCELA")],
        ]

        janela = sg.Window("Escolha de ataque", default_element_size=(40, 10)).Layout(layout)
        super(TelaJogadorArmas, self).cria_janela(janela)

    def mostra_tela(self, lista_de_armas):
        self.__armas = lista_de_armas
        return super().mostra_tela()