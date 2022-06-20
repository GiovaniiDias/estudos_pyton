sal = float(input("Digite seu salario: "))
if sal <= 1250:
    ad = sal + (sal * 15 /100)
else:
    ad = sal + (sal * 10 /100)
print("seu salario é de {:.2f}.".format(ad))