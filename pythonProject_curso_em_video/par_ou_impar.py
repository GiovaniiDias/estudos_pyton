numero = int(input("digite um numero"))
resultado = numero % 2
if resultado == 0:
    print("esse numero é par {}".format(resultado))
else:
    print("numero impar {}".format(resultado))