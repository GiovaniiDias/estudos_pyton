def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! por favor digite novamente!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuario finalizou!\033[m")
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! por favor digite novamente!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuario finalizou!\033[m")
            return 0
        else:
            return n


num = leiaint("digite um valor: ")
num2 = leiafloat("digite um valor: ")
print(f"O valor digitado foi {num} e {num2}")
