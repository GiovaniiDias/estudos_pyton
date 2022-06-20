galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("nome: "))
    while True:
        pessoa["sexo"] = str(input("sexo: [M/F] ")).upper()[0]
        if pessoa["sexo"] in "MF":
         break
        print("ERRO! apenas [M/F]")
    pessoa["idade"] = int(input("idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("continue? [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! apenas [S/N]")
    if resp == "N":
        break
print("-="*30)
print(f"ao todo temos {len(galera)} pessoas cadastradas")
media = soma / len(galera)
print(f"a media de idade é {media:5.2f} anos")
print(f"as mulheres cadastradas foram: ", end="  ")
for p in galera:
    if p["sexo"] in "fF":
        print(f"{p['nome']}", end="")
print()
print("lista acima da media")
for p in galera:
    if p["idade"] >= media:
        print("         ")
        for k, v in p.items():
            print(f"{k} = {v}: ", end=" ")
        print()
print("<<ENCERRADO>>")
