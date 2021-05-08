# Limites
from limite.telaGenerica2 import TelaGenerica

# Controles

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaArmaAltera(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__dados_da_arma = {
            "ID": None,
            "NOME": None,
            "DADOS": None,
            "FACES": None,
        }
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        id = self.__dados_da_arma["ID"]
        nome = self.__dados_da_arma["NOME"]
        dados = self.__dados_da_arma["DADOS"]
        faces = self.__dados_da_arma["FACES"]

        mensagem = f"Modificar arma: id: {id}, nome: {nome}"

        layout = [
            [sg.Text(mensagem, justification='center', size=(30, 2))],
            [sg.Text("Novo nome da arma:"), sg.InputText(nome, key="NOME")],
            [sg.Text("Nova quantidade de dados:"), sg.Slider(range=(1, 10), orientation='h', size=(10, 20), default_value=dados, key="DADOS")],
            [sg.Text("Novo numero de faces:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=faces, key="FACES")],
            [sg.Submit("Confirmar", key="CONFIRMA"), sg.Cancel("Cancelar", key="CANCELA")],
        ],

        janela = sg.Window("Alterar arma", default_element_size=(40, 10)).Layout(layout)
        super(TelaArmaAltera, self).cria_janela(janela)

    def mostra_tela(self, dados: dict):
        self.__dados_da_arma = dados
        return super().mostra_tela()
