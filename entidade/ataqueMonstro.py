

class AtaqueMonstro:
    def __init__(
        self,
        id: int,
        nome: str,
        quantidade_dado: int,
        numero_faces: int,
        dano_bonus: int,
        acerto: int,
        cd: int,
        teste: str
        ):
        self.__id = id
        self.__nome = nome
        self.__quantidade_dado = quantidade_dado
        self.__numero_faces = numero_faces
        self.__dano_bonus = dano_bonus
        self.__acerto = acerto
        self.__cd = cd
        self.__teste = teste

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def quantidade_dado(self):
        return self.__quantidade_dado

    @quantidade_dado.setter
    def quantidade_dado(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade_dado = quantidade

    @property
    def numero_faces(self):
        return self.__numero_faces

    @numero_faces.setter
    def numero_faces(self, dado: int):
        if isinstance(dado, int):
            self.__numero_faces = dado

    @property
    def dano_bonus(self):
        return self.__dano_bonus

    @dano_bonus.setter
    def dano_bonus(self, dano: int):
        if isinstance(dano, int):
            self.__dano_bonus = dano

    @property
    def acerto(self):
        return self.__acerto

    @acerto.setter
    def acerto(self, acerto: int):
        if isinstance(acerto, int):
            self.__acerto = acerto

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, cd: int):
        if isinstance(cd, int):
            self.__cd = cd

    @property
    def teste(self):
        return self.__teste

    @teste.setter
    def teste(self, teste: int):
        if isinstance(teste, int):
            self.__teste = teste
