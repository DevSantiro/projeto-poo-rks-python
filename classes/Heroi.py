import random

from classes.Personagem import Personagem


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome  = nome
        self.__vida  = vida
        self.__nivel = nivel


    def __str__(self) -> str:
        return f"Status do Herói: {self.__nome}, vida: {self.__vida}, nível: {self.nivel}"

    @property
    def nome(self) -> str:
        return self.__nome
    

    @property
    def vida(self) -> int:
        return self.__vida
    

    @property
    def nivel(self) -> int:
        return self.__nivel


    def ataque_normal(self, alvo):
        dano = random.choice(range(0, 20))
        alvo.dano_sofrido(dano=dano)
        print(f"{self.__nome} causou {dano} de dano em {alvo.nome} com o seu ataque normal.") 


    def ataque_especial(self, alvo):
        dano = random.choice(range(self.nivel, 20))
        alvo.dano_sofrido(dano=dano)
        print(f"{self.__nome} causou {dano} de dano em {alvo.nome} com o seu ataque especial.") 


    def dano_sofrido(self, dano: int) -> None:
        self.__vida -= dano


    def subir_nivel(self, nivel) -> int:
        self.__nivel += nivel
