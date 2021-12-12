# Chute e acerte o que o que o computador está pensando, ou vai pensar:

import random
from time import sleep # funciona com a funcionalidade sleep

while True:
    print("-=-"*30)
    while True:
        valor = int(input("Informe um valor de 0 a 5: "))
        if valor == 0 or valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5:
            break
        else:
            print("Você digitou um valor inválido!")
    num = random.randint(0,5)
    print("Estou pensando..!")
    sleep(1) # aqui faz o programa demorar um pouco só que vagarosamente
    if valor==num:
        print("Meus parabéns vc acertou! Eu pensei tbm em {}".format(num))
    else:
        print("Vc errou! eu pensei em {}".format(num))
    sleep(1)
    continuar = str(input("Você deseja jogar novamente? [S/N] ")).strip().upper()
    if "N" in continuar:
        break
    else:
        sleep(1)
        print("Ok vamos novamente então!")
        sleep(1)
sleep(1)
print("Tchau!")