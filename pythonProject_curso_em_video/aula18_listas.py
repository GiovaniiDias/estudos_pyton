'''teste = list()
teste.append("gustavo")
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = "maria"
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [["joão", 19], ["narcia", 12], ["aurelio", 15]]
print(galera[2][0])'''

'''galera = [["joão", 19], ["narcia", 12], ["aurelio", 15]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos")'''

'''galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input("nome")))
    dado.append(str(input("idade")))
    galera.append(dado[:])
    dado.clear()
print(galera)'''

'''galera = list()
dado = list()
totmai = totmeno = 0
for c in range(0, 3):
    dado.append(str(input("nome")))
    dado.append(int(input("idade")))
    galera.append(dado[:])
    dado.clear()'''

'''for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmeno +=1

print(f"temos {totmai} maiores e {totmeno} menores de idade.")'''