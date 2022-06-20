print(" gerador de PA:")
termo = int(input("digite o primeiro termo: "))
raz = int(input("digite a razão: "))
primeiro = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} > ".format(primeiro), end="")
        primeiro += raz
        cont += 1
    print("PAUSA")
    mais = int(input("quantos termos a mais? "))
print("finalizou com {} termos".format(total))
