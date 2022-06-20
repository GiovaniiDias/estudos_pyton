listagem = ("lapis", 1.75,
            "caneta" , 2.00,
            "caderno", 15.00,
            "livro", 12.00,
            "mochila", 50.00,
            "compasso", 9.99,
            "borracha", 0.50)
print("-"*40)
print(f'{"LISTA DE PREÇOS":^40}')
print("-"*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}",end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-="*40)