def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31m Erro! digite um numero valido!\33[m")
        if ok:
            break
    return valor

n = leiaInt("digite um numero: ")
print(f"vc digitou {n}")
