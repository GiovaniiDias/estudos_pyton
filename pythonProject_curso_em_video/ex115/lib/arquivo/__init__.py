from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArq(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("houve um erro na criação do arquivo!")
    else:
        print(f"arquivo {nome} criado com sucesso!")
def lerArq(nome):
    try:
        a = open(nome, "rt")
    except:
        print("erro ao ler arquivo")
    else:
        cabeçalho("Usuarios cadastrados:")
        print(a.read())

