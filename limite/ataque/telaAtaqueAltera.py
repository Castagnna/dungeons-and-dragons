# Limites
from limite.telaGenerica2 import TelaGenerica

# Controles

# Utils
from PySimpleGUI import PySimpleGUI as sg


class TelaAtaqueAltera(TelaGenerica):

    def __init__(self, controlador):
        super().__init__(controlador)
        self.__dados_da_ataque = {
            "ID": None,
            "NOME": None,
            "DADOS": None,
            "FACES": None,
            "BONUS": None,
            "ACERTO": None,
            "CD": None,
            "TESTE": None,
        }
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')

        testes = [
            "Forca", "Destreza", "Constituicao", 
            "Sabedoria", "Inteligencia", "Carisma", "Nenhum"
        ]

        id = self.__dados_da_ataque["ID"]
        nome = self.__dados_da_ataque["NOME"]
        dados = self.__dados_da_ataque["DADOS"]
        faces = self.__dados_da_ataque["FACES"]
        bonus = self.__dados_da_ataque["BONUS"]
        acerto = self.__dados_da_ataque["ACERTO"]
        cd = self.__dados_da_ataque["CD"]
        teste = self.__dados_da_ataque["TESTE"]

        mensagem = f"Modificar ataque: id: {id}, nome: {nome}"

        layout = [
            [sg.Text(mensagem, justification='center', size=(30, 2))],
            [sg.Text("Novo nome da ataque:"), sg.InputText(nome, key="NOME")],
            [sg.Text("Nova quantidade de dados:"), sg.Slider(range=(1, 10), orientation='h', size=(10, 20), default_value=dados, key="DADOS")],
            [sg.Text("Novo numero de faces:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=faces, key="FACES")],
            [sg.Text("Novo dano bonus:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=bonus, key="BONUS")],
            [sg.Text("Novo acerto:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=acerto, key="ACERTO")],
            [sg.Text("Novo CD:"), sg.Slider(range=(1, 20), orientation='h', size=(10, 20), default_value=cd, key="CD")],
            [sg.Text("Novo teste:"), sg.InputCombo(testes, size=(14, 1), default_value=teste, key="TESTE")],
            [sg.Submit("Confirmar", key="CONFIRMA"), sg.Cancel("Cancelar", key="CANCELA")],
        ],

        janela = sg.Window("Alterar ataque", default_element_size=(40, 10)).Layout(layout)
        super(TelaAtaqueAltera, self).cria_janela(janela)

    def mostra_tela(self, dados: dict):
        self.__dados_da_ataque = dados
        return super().mostra_tela()
