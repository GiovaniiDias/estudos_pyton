from datetime import date
ano = int(input("qual ano quer avaliar?  Coloque 0 para avaliar o ano atual: "))
if ano == 0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("o ano {} é bixeto.".format(ano))
else:
    print("o ano {} NÃO é bixesto".format(ano))