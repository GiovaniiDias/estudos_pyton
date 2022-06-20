cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis ",
        "sete", "oito", "nove", "dez", "onze", "doze",
        "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")
while True:

    num = int(input("digite um numero de 0 a 20: "))
    if  0 <= num <= 20:
        break
    print("tente novamente. ", end="")
print(f"vc digitou {cont[num]}")
