from time import sleep


def contador(i, f, p):

    print(f"contagem de {i} até {f} de {p} em {p}.")

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ",end=" ", flush=True)
            sleep(0.5)
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ",end=" ", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")



contador(1, 10, 1)

contador(10, 1, 1)

print("Agora é com vc!")
ini = int(input("Inicio: "))
fim = int(input("Fim:    "))
pas = int(input("Passo: "))
contador(ini, fim, pas)