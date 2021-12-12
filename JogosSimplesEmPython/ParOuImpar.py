# Você e o computador informarão cada qual um valor entre 0 e 50, no final serão somados os valores e o resultado decidirá o vencedor
# E conforme as vitórias do jogador, você poderá jogar novamente
import random
from time import sleep

print("-=-"*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-"*20)
cont = 0
valor = 0
escolha = " " # É necessário que este espaço não esteja nulo como escolha = ""
comp = 0

while True:
    valor = int(input("Diga um valor: "))
    while escolha not in "PI": #Serve para caso digite um caracter fora do que foi determinado ele repita o mesmo comando até que o certo seja digitado
        escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    comp = random.randint(0, 51)
    soma = comp + valor
    sleep(2)
    print("-"*60)
    print(f"Você jogou {valor} e o computador {comp}. Total de {soma} ", end="")
    sleep(2)
    if escolha == "P":
        if soma % 2 == 0:
            print("DEU PAR")
            print("-" * 60)
            print("Você VENCEU!")
            sleep(2)
            print("Vamos jogar novamente...")
            sleep(2)
            cont += 1
        else:
            print("DEU IMPAR")
            print("-" * 60)
            print("Você PERDEU!")
            print("-=-" * 20)
            sleep(2)
            print(f"GAME OVER! Você venceu {cont} vezes")
            break
    elif escolha == "I":
        if soma % 2 == 0:
            print("DEU PAR")
            print("-" * 60)
            print("Você PERDEU!")
            print("-=-" * 20)
            sleep(2)
            print(f"GAME OVER! Você venceu {cont} vezes")
            break
        else:
            print("DEU IMPAR")
            print("-" * 60)
            print("Você VENCEU!")
            sleep(2)
            print("Vamos jogar novamente...")
            sleep(2)
            cont += 1
    escolha = " "
    print("-"*60)