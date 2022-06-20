valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
opc = 0
while opc !=5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair''')
    opc = int(input("qual sua escolha?"))
    if opc == 1:
                soma = valor1 + valor2
                print(soma)

    elif opc == 2:
                prod = valor1 * valor2
                print(prod)
    elif opc == 3:
        if valor1 > valor2:
               maior = valor1
        else:
             maior = valor2
             print(maior)
    elif opc == 4:
                print("informe novamente")
                valor1 = int(input("valor 1"))
                valor2 = int(input("valor 2"))

    elif opc == 5:
                print("finalizando")

    else:
            print("opção invalida")
