# JO KEN PO, ou pedra, papel e tesoura no linguajar popular:

from time import sleep
import random

while True:
    print("-=-" * 10)
    while True:
        print("Você está duelando contra o computador!")
        escolha = int(input("Escolha Pedra-1|Papel-2|Tesoura-3: "))
        if escolha == 1 or escolha == 2 or escolha == 3:
            break
        else:
            print("Você digitou um valor inválido!")
    print("Vocês se encaram", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".")
    escolhapc = random.randint(1,3)
    if escolhapc == 1:
        J = "Pedra"
    elif escolhapc == 2:
        J = "Papel"
    else:
        J = "Tesoura"
    sleep(2)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!")
    sleep(1)
    print(f"Computador escolhe {escolhapc} - {J}")
    sleep(1)
    print("-=-"*10)
    if escolha == escolhapc:
        print("DEU EMPATE!")
    elif (escolha == 1) and (escolhapc == 2):
        print("VITORIA DO COMPUTADOR!")
    elif (escolha == 1) and (escolhapc == 3):
        print("VITORIA DO JOGADOR!")

    elif (escolha == 2) and (escolhapc == 1):
        print("VITORIA DO JOGADOR!")
    elif (escolha == 2) and (escolhapc == 3):
        print("VITORIA DO COMPUTADOR!")

    elif (escolha == 3) and (escolhapc == 1):
        print("VITORIA DO COMPUTADOR!")
    elif (escolha == 3) and (escolhapc == 2):
        print("VITORIA DO JOGADOR!")
    sleep(1)
    print("-=-" * 10)
    continuar = str(input("Você deseja jogar novamente? [S/N] ")).strip().upper()
    if "N" in continuar:
        break