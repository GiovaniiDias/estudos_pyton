ficha = list()
while True:
    nome = str(input("nome"))
    n1 = float(input("nota 1"))
    n2 = float(input("nota 2"))
    media = (n1 + n2) / 2
    ficha.append([nome,[n1, n2], media])
    resp = str(input("quer cont? [S/N]..."))
    if resp in "Nn":
        break
print("-="*30)
print(f'{"No.":<4}{"nome":<10}{"media":>8}')
print("-="*26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}" )
while True:
    print("-"*30)
    opc = int(input("mostrar nota de qual aluno? (999 para)"))
    if opc == 999:
        print("finalizando...")
        break
    if opc <= len(ficha) -1:
        print(f"notas de {ficha [opc] [0]} são {ficha [opc] [1]}")
print("FIM")

