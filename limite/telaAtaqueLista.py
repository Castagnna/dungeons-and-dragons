# Limites
from limite.telaGenerica2 import TelaGenerica

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaAtaqueLista(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__lista_de_ataques = []
        self.init_components()

    @staticmethod
    def monta_lista_str(lista_de_ataques: list):

        def monta_string(id, nome, dados, faces, bonus, acerto, cd, teste):
            return f"{id:^4}|{nome:^14}|{dados:^9}|{faces:^6}|{bonus:^6}|{cd:^6}|{teste:^10}"

        lista_str = [" Id |   Nome   | Dados | Faces | Bonus | cd | teste"]
        
        for ataque in lista_de_ataques:
            string = monta_string(
                ataque.id,
                ataque.nome,
                ataque.quantidade_dado,
                ataque.numero_faces,
                ataque.dano_bonus,
                ataque.acerto,
                ataque.cd,
                ataque.teste,
            )
            lista_str.append(string)

        return lista_str

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        valores = self.monta_lista_str(self.__lista_de_ataques)

        layout = [
            [sg.Listbox(values=valores, size=(50, 6))],
            [sg.Cancel("OK", key="OK")],
        ]

        janela = sg.Window("Lista de ataques", default_element_size=(40, 10)).Layout(layout)
        super(TelaAtaqueLista, self).cria_janela(janela)

    def mostra_tela(self, lista_de_ataques):
        self.__lista_de_ataques = lista_de_ataques
        return super().mostra_tela()
