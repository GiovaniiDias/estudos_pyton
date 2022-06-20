from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = "cursoemvideo.txt"
if arquivoExiste(arq):
    print("arquivo encontrado com sucesso")
else:
    print("arquivo não encontrado")
    criarArq(arq)

while True:
    res = menu(["Ver usuario cadastradas", "Cadastrar novo usuario", "Sair"])
    if res == 1:
       lerArq(arq)
    elif res == 2:
        print("opc2")
    elif res == 3:
        print("Desconectando...")
        break
    else:
        print("\033[31mERRO! digite 1, 2 ou 3..\033[m")