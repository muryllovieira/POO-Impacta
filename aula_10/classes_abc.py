from abc import ABC, abstractmethod


class MinhaClasseAbstrata(ABC):
    @staticmethod
    @abstractmethod
    def meu_metodo_estatico_abstrato():
        pass

    @classmethod
    @abstractmethod
    def meu_metodo_de_classe_abstrato(cls):
        pass
