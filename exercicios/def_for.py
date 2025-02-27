#######################
# Ex. 4


def percorrerListaComFor(lista, alvo):
    for i, a in enumerate(lista):
        if a == alvo:
            return i
        else:
            continue
    return "Alvo não encontrado!"


lista = [10, 20, 30, 40, 50]

print(percorrerListaComFor(lista, alvo=30))
