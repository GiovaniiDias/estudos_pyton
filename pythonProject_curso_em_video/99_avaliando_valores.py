def maior(* num):
    cont = maior = 0
    print("\nanalizando os valores passados")
    for valor in num:
        print(f"{valor} ", end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"foram informados {cont} valores ")
    print(f"o maior é {maior}")


maior(2, 9, 7, 1)
maior(8, 2, 6, 3)
maior(2, 6, 5, 4)
maior(4)
maior()
