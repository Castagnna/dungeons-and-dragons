from dao.daoContador import ContadorDAO


class CombateContadorDAO(ContadorDAO):

    def __init__(self):
        super().__init__("combate_contador.pkl")
