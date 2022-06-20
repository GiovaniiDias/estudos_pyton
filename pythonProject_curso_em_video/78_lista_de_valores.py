listan = list()
maior = 0
menor = 0
for c in range(0, 5):
    listan.append(int(input(f"digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = listan[c]
    else:
        if listan[c] > maior:
            maior = listan[c]
        if   listan[c] < menor:
            menor = listan[c]

print("=="*30)
print(f"vc digitou os valores {listan}")
print(f"o maior valor é {maior} nas posições ", end="")
for i, v in enumerate(listan):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"o menor valor é {menor} nas posições ", end="")
for i, v in enumerate(listan):
    if v == menor:
        print(f"{i}...", end="")
print()