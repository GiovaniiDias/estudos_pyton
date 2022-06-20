print(" gerador de PA:")
termo = int(input("digite o primeiro termo: "))
raz = int(input("digite a razão: "))
primeiro = termo
cont = 1
while cont <= 10:
    print("{} > ".format(primeiro), end="")
    primeiro += raz
    cont += 1
print("fim")