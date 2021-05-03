from dao.daoContador import ContadorDAO


class MonstroContadorDAO(ContadorDAO):

    def __init__(self):
        super().__init__("monstro_contador.pkl")
