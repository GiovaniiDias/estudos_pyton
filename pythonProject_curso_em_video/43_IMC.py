peso = float(input("Digite seu peso atual: "))
alt = float(input("Digite sua altura atual: "))
imc = peso / (alt ** 2)
print("imc = {:.1f}".format(imc))
if imc < 18.5:
    print("baixo do peso")
elif imc< 25:
    print("peso ideal")
elif imc< 30:
    print("sobrepeso")
elif  imc < 40:
    print("obesidade")
elif imc > 40:
    print("obesidade mórbida")