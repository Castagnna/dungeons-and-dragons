import pickle
from abc import ABC, abstractmethod


class ContadorDAO(ABC):

    @abstractmethod
    def __init__(self, data_source=""):
        self.__data_source = data_source
        self.__cache = 0
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__data_source, "wb"))

    def __load(self):
        self.__cache = pickle.load(open(self.__data_source, "rb"))

    def add(self, valor: int=1):
        if isinstance(valor, int):
            self.__cache += valor
            self.__dump()

    def reset(self, valor: int = 0):
        if isinstance(valor, int):
            self.__cache = valor
            self.__dump()
    
    def get(self) -> int:
        return self.__cache
