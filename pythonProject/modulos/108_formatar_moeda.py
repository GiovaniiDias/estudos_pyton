from ex108 import moeda

p = float(input("digite um numero: "))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"A aumentando 10% temos, {moeda.moeda(moeda.aumentar(p, 10))}")