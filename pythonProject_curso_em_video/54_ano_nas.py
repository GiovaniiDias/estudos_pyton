from datetime import date
atual = date.today().year
totmai = 0
totmen = 0
for c in range(1, 4):
    num = int(input("digite o ano de nasc: "))
    men = atual - num
    if men >= 21:
        totmai += 1
    else:
        totmen += 1
print("{} pessoas MAIOR".format(totmai))
print("{} pessoas MENOR".format(totmen))