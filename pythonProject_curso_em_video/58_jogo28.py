from random import randint
com = randint(0, 10)
print("qual numero eu pensei de 0 a 10? ")
acertou = False
palpite = 0
while not acertou:
    jog = int(input("qual seu palpite? "))
    palpite += 1
    if jog == com:
        acertou = True
    else:
        if jog < com:
            print("ta frio")
        elif jog > com:
            print("ta quente")
print("acetrou com {} tentativas".format(palpite))