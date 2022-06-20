sexo = str(input("qual sexo: [M/F]")).strip().upper()[0]
while sexo not in "MFmf":
    sexo = str(input("dadosinvalidos. digite novamente")).strip().upper()[0]
print(sexo)
