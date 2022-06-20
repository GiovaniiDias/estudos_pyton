valores = []
while True:
    valores.append(int(input("digite um valor: ")))
    resp = str(input("quer continuar ? [S/N] "))
    if resp in "Nn":
        break
print("="*30)
print(f"vc digitou {len(valores)} elementos")
valores.sort(reverse=True)
print(f"em ordem decrescente {valores}")
if 5 in valores:
    print("o valor 5 faz parte da lista")
else:
    print("5 não foi encontardo")