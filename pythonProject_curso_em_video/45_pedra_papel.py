from random import randint
from time import sleep
itens = ("pedra", "papel", "tesoura")
comp = randint(0, 2)
print(''' suas opções
[0] pedra
[1] papel
[2] tesoura''')
jog = int(input("qual é a sua jogada?"))
print("JOOO")
sleep(1)
print("KEN")
sleep(1)
print("POO!!")
sleep(1)
print("computador jogou {}".format(itens[comp]))
print("jogador jogou {}".format(itens[jog]))
if comp == 0:
    if jog == 0:
        print("empate")
    elif jog == 1:
        print("jogador vence")
    elif jog == 2:
        print("computador vence")
    else:
        print("jogada invalida")

elif comp == 1:
    if jog == 0:
     print("computador vence")
    elif jog == 1:
     print("empate")
    elif jog == 2:
      print("jogador vence")
    else:
     print("jogada invalida")
elif comp == 2:

    if jog == 0:
     print("jogador vence")
    elif jog == 1:
     print("computador vence")
    elif jog == 2:
     print("empate")
else:
    print("jogada invalida")
