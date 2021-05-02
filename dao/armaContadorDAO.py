from dao.daoContador import ContadorDAO


class ArmaContadorDAO(ContadorDAO):

    def __init__(self):
        super().__init__("arma_contador.pkl")
