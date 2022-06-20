n1 = float(input("digite a primera nota: "))
n2 = float(input("digite a segunda nota: "))
media = (n1 + n2) / 2
if media <= 5.0:
    print("vc não alcançou a média!")
elif media <= 6.9:
    print("recuperação!")
else:
    print("aprovado!")