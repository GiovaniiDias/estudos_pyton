numeros = list()
while True:
    n = int(input("digite um valor:"))
    if n not in numeros:
        numeros.append(n)
        print("Value sucefull")
    else:
        print("Duplicat value! Not add." )
    r = str(input("quer continuar?"))
    if r in "Nn":
        break
print("=-"*30)
print("+-"*30)
print("+-"*30)
print("=_"*30)
numeros.sort()
print(f"vc digitou {numeros}")