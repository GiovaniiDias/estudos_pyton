print("-=" * 20)
print("avaliar um triangulo:")
print("-=" * 20)
r1 = float(input("digite o 1°"))
r2 = float(input("digite o 2°"))
r3 = float(input("digite o 3°"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print(" forma um triangulo .")
if r1 == r2 == r3:
    print("é um EQUILATERO")
elif r1== r2:
    print(" é um ISOSCELES")
elif r1 == r3:
    print(" é um ISOSCELES")
elif r2 == r3:
    print(" é um ISOSCELES")
else:
    print("NÃO forma!")