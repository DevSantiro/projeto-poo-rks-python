from abc import ABC, abstractmethod

class Personagem(ABC):

    @abstractmethod
    def ataque_normal(self):
        pass

    @abstractmethod
    def dano_sofrido(self):
        pass
