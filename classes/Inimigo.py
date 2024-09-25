import random

from classes.Personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo = "Inimigo") -> None:
        self.__nome  = nome
        self.__vida  = vida
        self.__nivel = nivel
        self.__tipo  = tipo


    def __str__(self) -> str:
        return f"Status do Inimigo: {self.__nome}, vida: {self.__vida}, nível: {self.nivel}"

    @property
    def nome(self) -> str:
        return self.__nome
    

    @property
    def vida(self) -> int:
        return self.__vida
    

    @property
    def nivel(self) -> int:
        return self.__nivel
    

    @property
    def tipo(self) -> str:
        return self.__tipo


    def ataque_normal(self, alvo):
        dano = random.choice(range(0, 20))
        alvo.dano_sofrido(dano=dano)
        print(f"Inimigo: {self.__nome} causou {dano} de dano em {alvo.nome} com o seu ataque normal.") 


    def dano_sofrido(self, dano: int) -> None:
        self.__vida -= dano
