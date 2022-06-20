def fatorial(n, show=False):
    """
    -> calcula o fatorial
    :param n: o numero a ser calculado
    :param show:opcional , mostrar ou não a conta
    :return:o valor do fatorial n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


fat = int(input("digite um numero: "))
print(fatorial({f"{fat}, show=True"))