print("-_" *20)
print("Simulador de emprestimo")
print("-_" *20)

vcasa = float(input("Qual o valor desejado? "))
sal = float(input("Qual seu salario? "))
tem = int(input("Quantos anos para pagar? "))
pre =  vcasa/ (tem * 12)
min = sal * 30 / 100
if pre <= min:
    print("Emprestimo aprovado!")
else:
    print("NEGADO!")
