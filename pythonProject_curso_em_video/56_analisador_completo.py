somaid = 0
media = 0
totmu20 = 0
for c in range(1, 5):
    print("------{}° PESSOA-------".format(c))
    nome = str(input("nome: ")).strip()
    idade = int(input("idade: "))
    sexo = str(input("sexo [M/F]: ")).strip()
    somaid += idade
    if c == 1 and sexo in "mM":
          maioridade = idade
          nomesenior = nome
    if sexo in"mM" and idade > maioridade:
        maioridade = idade
        nomesenior = nome
        if sexo in "Ff" and idade < 20:
            totmu20 += 1

media = somaid / 4


print("idade média é de {}".format(media))
print("homem velho {} anos e se chama {}".format(maioridade, nomesenior))
print("ao todo são {} mulheres menores de 20 anos".format(totmu20))

