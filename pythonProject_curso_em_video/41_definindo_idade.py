from datetime import date
atual = date.today().year
ano = int(input("Digite o ano do seu nascimento:"))
cat = atual - ano
if cat <= 9:
    print(" CATEGORIA MIRIM")
elif cat <= 14:
    print(" CATEGORIA INFANTIL")
elif cat <= 19:
    print(" CATEGORIA JUNIOR")
elif cat <=20:
    print(" CATEGORIA SENIOR")
elif cat > 20:
    print(" CATEGORIA MASTER")