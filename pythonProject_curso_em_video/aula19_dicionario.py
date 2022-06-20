'''pessoas = {"nomes": "gustavo", "sexo": "M", "idade": 22}
print(pessoas.keys())'''

'''pessoas = {"nomes": "gustavo", "sexo": "M", "idade": 22}
print(pessoas.items())'''

'''pessoas = {"nomes": "gustavo", "sexo": "M", "idade": 22}
print(pessoas.values())'''

'''pessoas = {"nomes": "gustavo", "sexo": "M", "idade": 22}
for k, v in pessoas.items():
    print(f"{k} = {v}")'''

'''brasil = []
estado = {"uf": "rio", "sigla": "rj" }
estado2 = {"uf": "sao", "sigla": "sp"}
brasil.append(estado)
brasil.append(estado2)

print(brasil)
print(estado)'
print(estado2)'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("UF: "))
    estado["sigla"] = str(input("sigla do estado: "))
    brasil.append(estado.copy())
for c in brasil:
    for k, v in c.items():
        print(f"o campo {k} tem valor {v}")