'''from math import  factorial
n = int(input("digite um numeero: "))
f = factorial(n)
print("o fatorial de {} é {}".format(n, f))'''

n = int(input("digite um numeero: "))
c = n
f = 1
print("calculando {}! = ".format(n), end="")
while c > 0:
    print("{} x ".format(c), end="")
    print("x" if c > 1 else "=", end="")
    f *= c
    c -= 1
print("{}".format(f))

#print("o fatorial de {} é {}".format(n, f))

