from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)
for num in n:
    print(f"{num}", end="")
print(f"o maior foi {max(n)}", end="")
print(f"o menor foi {min(n)}", end="")