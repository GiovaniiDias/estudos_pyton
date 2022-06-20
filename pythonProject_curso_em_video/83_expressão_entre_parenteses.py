exp = str(input("difgite a expressão: "))
pilha = []
for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("expressão valida!")
else:
    print("expressão incorreta!")