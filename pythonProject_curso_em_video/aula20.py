def soma(a, b):
    s = a + b
    print(f" {a} + {b} = {s} ")
def contador(* num):
    for v in num:
        print(f"{v}", end=" ")
    print("fim")


#programa principal
soma(4, 5)
soma(2, 7)
soma(8, 6)

contador(1, 0, 2, 3, 4, )
contador(3, 5, 4, 6, 7,)
contador(2, 3)

