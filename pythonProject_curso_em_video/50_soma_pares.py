soma = 0
cont = 0
for c in range(1, 7):
    num = int(input("digite seis numeros: "))
    if num % 2 == 0:
         soma = soma + num
         cont += 1
print(soma)