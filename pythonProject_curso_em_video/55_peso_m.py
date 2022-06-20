pesmai = 0
pesmen = 0
for c in range(1, 4):
    pes = float(input("{}° digite seu peso: ".format(c)))

    if c == 1:
        pesmai = pes
        pesmen = pes
    else:
        if pes > pesmai:
            pesmai = pes
        if pes < pesmen:
                pesmen = pes
print("{} peso MAIOR".format(pesmai))
print("{} peso MENOR".format(pesmen))