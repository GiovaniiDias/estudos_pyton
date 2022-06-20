time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["nome"] = str(input("nome do jogador: "))
    tot = int(input(f"quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"quantos gols na partida {c}? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("continue?  [S/N]")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! APENAS S OU N!")
    if resp == "N":
        break
print("-="*30)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-="*30)
for k, v in enumerate(time):
    print(f"{k:>3}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("-="*30)
while True:
    busca = int(input("mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
      print(f"ERRO! JOGADOR INEXISTENTE {busca}!")
    else:
        print(f"levantamento do jogador {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"      no jogo {i+1} fez {g} gols.")
    print("-=" * 30)


print("-="*30)
for k, v in jogador.items():
    print(f"o campo {k} tem o valor {v}")
print("-="*30)
print(f"o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for i, v in enumerate(jogador["gols"]):
    print(f"   => na partida {i+1} fez {v} gols ")
print(f"total de {jogador['total']} gols")