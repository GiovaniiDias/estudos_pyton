from datetime import date
atual = date.today().year
nas = int(input("Qual ano dos eu nascimento? "))
idade = atual - nas
print("quem nasceu em {} tem {} em {}.".format(nas, idade, atual))
if idade == 18:
    print("vc tem q se alistar imediatammente!")
elif idade < 18:
    saldo = 18 - idade
    ano = atual - saldo
    print("ainda faltam {} anos para se alistar.".format(saldo))
    print("seu alistamento será em {}.".format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print("vc já deveria ter se alistado há {} anos.".format(saldo))
    print("seu ano de alistamento foi em {}.".format(ano))