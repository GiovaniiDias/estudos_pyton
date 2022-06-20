num = [[], []]
valor = 0
for c in range(0, 8):
    valor = int(input("digite um valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("=-"*30)
num[0].sort()
num[1].sort()
print(f"pares {num[0]}")
print(f"impares {num[1]}")