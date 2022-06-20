cidade = str(input("digite o nome da cidade: ")).strip()
nome = cidade.split()
print("nome {} ".format(nome[0]))
print("sobrenome {}".format(nome[len(nome)-1]))