def ficha(jog="<desconhecido>", gol=0):
    print(f"o jogador {jog} fez {gol} gol(s)")

nome = str(input("nome do cara: "))
g = str(input("quantos gols? "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == "":
    ficha(gol=g)
else:
    ficha(nome, g)




