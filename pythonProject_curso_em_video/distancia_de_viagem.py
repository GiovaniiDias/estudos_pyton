km = float(input("quantos km vai viajar? "))
if km <= 200:
    valor = 0.50 * km
else:
    valor = 0.45 * km
print("valor é {:.2f}.".format(valor))