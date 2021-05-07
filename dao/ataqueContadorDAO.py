from dao.daoContador import ContadorDAO


class AtaqueContadorDAO(ContadorDAO):

    def __init__(self):
        super().__init__("ataque_monstro_contador.pkl")
