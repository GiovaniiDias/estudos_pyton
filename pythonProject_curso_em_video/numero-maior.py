n1 = int(input("digite 1° numero: "))
n2 = int(input("digite 2° numero: "))
if n1 < n2:
    print("o {} é menor que o {}.".format(n1,n2))
elif n2 < n1:
    print("o {} é menor que o {}.".format(n2, n1))
else:
    print("Os numeros são iguais")