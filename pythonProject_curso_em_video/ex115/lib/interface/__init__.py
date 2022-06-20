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

def linha(tam = 42):
    return "-" * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho("Menu principal")
    c = 1
    for iten in lista:
        print(f"{c} - {iten}")
        c += 1
    print(linha())
    opc = leiaint("Sua opção: ")
    return opc
