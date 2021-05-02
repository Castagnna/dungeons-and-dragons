from dao.daoContador import ContadorDAO


class JogadorContadorDAO(ContadorDAO):

    def __init__(self):
        super().__init__("jogador_contador.pkl")
