def area(larg, comp):
    a = larg * comp
    print(f"A area de um terreno {larg} x {comp} = {a}m².")


print("-="*20)
print("controle de metragem")
l = float(input("largura (a): "))
c = float(input("comprimento (m): "))
area(l, c)