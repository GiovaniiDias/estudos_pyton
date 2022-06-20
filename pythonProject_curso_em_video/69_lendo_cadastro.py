tot18 = toth= totm = 0
while True:
    idade = int(input("idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("sexo: ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        toth += 1
    if sexo == "F" and idade < 20:
        totm += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Continue?: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"total maiores: {tot18}")
print(f"ao todo temos {toth} de homens cadastrados")
print(f"ao todo temos {totm} de mulheres com nemos de 20")