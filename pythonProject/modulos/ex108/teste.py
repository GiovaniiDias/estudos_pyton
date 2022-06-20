import moeda

p = float(input("digite um numero: "))
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumantando 10%, temos {moeda.aumentar(p, 10)}")