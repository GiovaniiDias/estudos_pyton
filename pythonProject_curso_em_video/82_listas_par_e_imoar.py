num = list()
pares = list()
impares = list()
while True:
    num.append(int(input("digite um numero:")))
    resp = str(input("quer continuar? [S/N]"))
    if resp in "Nn":
        break
for i, v in enumerate(num):
    if v % 2 == 0 :
        pares.append(v)
    elif v% 2 == 1:
        impares.append(v)
print("=+"*30)
print(f"lista completa é {num}")
print(f"lista de pares {pares}")
print(f"lista de impares {impares}")
