valor = float(input("qual valor?"))
print('''selecione a forma de pagamento
[1] dineiro
[2] cartão a vista
[3] 2x no cartão
[4] 3x no cartão
''')
pag = int(input("qual a opção de pagamento?"))
if pag == 1:
   total = valor - (valor * 10/100)
elif pag == 2:
print("Sua compra de R${:.2f} vai custar R${:.2f}".format(valor,  valor - (valor * 5 / 100))
if pag == 3:
    parc = valor / 2
    print("sua compra de R$ {:.2f} sera parcelada em 2x de R${:.2f}".format(valor, parc))

if pag == 4:
    total = valor + (valor * 20/100)
    totparc = int(input("quantas parcelas?"))
    parc = total / totparc
print("Sua compra de R${:.2f} vai custar R${:.2f}".format(valor, total))