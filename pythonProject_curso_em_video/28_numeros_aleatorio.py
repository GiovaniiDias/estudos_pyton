from random import randint
comp = randint(0,5)
print("-=-" *20)
print("vou pensar em um numero de 0 a 5")
print("-=-" *20)
n1 = int(input("qual numero?"))
if n1 == comp:
    print("isso")
else:
    print("errou")