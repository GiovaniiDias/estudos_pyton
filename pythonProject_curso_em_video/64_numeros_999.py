num = cont = soma = 0
num = int(input("digite [999 para parar]: "))
while num != 999:

    soma += num
    cont += 1
    num = int(input("digite [999 para parar]: "))
print("vc digitou {} numeros a soma deles é {} ".format(cont, soma))