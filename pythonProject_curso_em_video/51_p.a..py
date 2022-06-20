pr = int(input("primeiro termo: "))
raz = int(input("Razão: "))
dec = pr + (10 - 1) * raz
for c in range(pr, dec + raz, raz):
    print("{}".format(c), end=" -> ")
print("fim")