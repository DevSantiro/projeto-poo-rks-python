import random
from classes.Inimigo import Inimigo
from classes.Heroi import Heroi

# Função para criar novos inimigos dinamicamente
def criar_inimigo(nivel_heroi):
    if nivel_heroi in range(1, 5):
        return Inimigo(nome="Comum", vida=5*random.choice(range(1, 4)), nivel=random.choice(range(1, 4)))
    elif nivel_heroi in range(5, 10):
        return Inimigo(nome="Comum", vida=5*random.choice(range(5, 9)), nivel=random.choice(range(1, 4)))
    elif nivel_heroi in range(10, 15):
        return Inimigo(nome="Comum", vida=5*random.choice(range(10, 14)), nivel=random.choice(range(1, 4)))
    elif nivel_heroi in range(15, 20):
        return Inimigo(nome="Comum", vida=5*random.choice(range(15, 19)), nivel=random.choice(range(1, 4)))
    else:
        return Inimigo(nome="Comum", vida=5*20, nivel=20)

# Inicializando o herói
heroi = Heroi(nome="Heroi", vida=50, nivel=1)

continuar = True
rodadas = 0

while heroi.vida > 0 and continuar:
    
    # Criar um novo inimigo com base no nível do herói
    inimigo = criar_inimigo(heroi.nivel)
    
    # Loop de combate
    while inimigo.vida > 0 and heroi.vida > 0:
        rodadas += 1
        print(f"####### Turno: {rodadas} #######")

        heroi.ataque_normal(alvo=inimigo)
        inimigo.ataque_normal(alvo=heroi)

        print(heroi)
        print(inimigo)

        if heroi.vida <= 0:
            print(f"\nInfelizmente o {heroi.nome} morreu em combate.")
            continuar = False
            break

        if inimigo.vida <= 0:
            heroi.subir_nivel(1)
            print(f"O herói venceu o combate e passou de nível!")

            # Pergunta se deseja continuar a jornada
            try:
                continuar = True if int(input("Deseja continuar a jornada? [1 - Sim, 0 - Não] ")) == 1 else False
                break

            except Exception:
                continuar = False
                break


print("Encerrando a partida, resultado final do Herói: ")
print(heroi)
print(f"Total de {rodadas} rodadas.")
