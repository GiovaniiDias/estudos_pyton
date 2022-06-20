from random import randint
from time import sleep
lista = list()
jogos = list()
print("-="*30)
print("SORTEIO DA MEGA SENA")
print("-="*30)
quat = int(input("quantos jogos quer fazer? "))
tot = 1
while tot <= quat:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"-=" * 3, f"SOERTEANDO {quat} JOGOS ", "-="*3)
for i, l in enumerate(jogos):
    print(f" jogo {i+1}: {l}")
    sleep(1)
print(f"-=" * 5, f"<Boa Sorte!>", "-="*5)