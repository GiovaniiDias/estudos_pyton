n1 = (int(input("digite um numero: ")),
    int(input("digite um numero: ")),
    int(input("digite um numero: ")),
    int(input("digite um numero: ")))

print(f"vc digitou {n1}")
print(f"o valor  9 apareceu {n1.count(9)} vezes")
if 3 in n1:
    print(f" o 3 apareceu na {n1.index(3)+1} posição")
else:
    print("o valor 3 não foi digitado!")
print("os valores pares digitados foram ", end="")
for n in n1:
    if n % 2 == 0:
        print(n, end=" ")