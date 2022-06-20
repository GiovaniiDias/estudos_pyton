from random import randint
v = 0
while True:
    jog = int(input("digite um numero: "))
    comp = randint(0, 10)
    total = jog + comp
    tipo = " "
    while tipo not in "PpIi":
        tipo = str(input("Par ou Impar [P/I}? ")).strip().upper()[0]
    print(f"vc jogou {jog} e o computador jogou {comp}. total = {total}")
    if tipo == "P":
            if total % 2 == 0:
                print("VENCEU")
                v += 1
            else:
                print("PERDEU")
                break
    elif tipo == "I":
            if total % 2 == 1:
                print("VENCEU")
                v += 1
            else:
                print("PERDEU")
                break
    print("vamos jogar novamente...")
print(f"GAME OVER... VOCRE VENCEU {v} x")
