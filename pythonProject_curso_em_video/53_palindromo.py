fra = str(input("digite uma frase: ")).strip().upper()
pal = fra.split()
jun = "".join(pal)
inv = ""
for letra in range(len(jun)-1 , -1, -1):
    inv += jun[letra]
print("o inverso de {} é {}".format(jun, inv))
if inv == jun:
        print("PALINDROMO!")
else:
        print("NÃO É PALINDROMO!")
