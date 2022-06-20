nome = str(input("digite seu nome completo: ")).strip()
print("Analizando seu nome...")
#nome com letras maiusculas e minusculas
print("seu nome em maiusculas, tem: {}".format(nome.upper()))
print("seu nome em minusculas, tem: {}".format(nome.lower()))
#quantas letras tem
print("seu nome tem {} letras".format(len(nome) - nome.count(" ")))
#quantas letras tem o primeiro nome
print("seu primeiro nome tem  {} letras".format(nome.find(" ")))