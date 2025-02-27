###################################################
# Exercício N°5

listinha = [10, 20, 30, 40, 50]


def percorrerListaWhile(lista, alvo):
    iterador = 0
    while len(lista) > iterador:
        iterador += 1
        if lista[iterador] == alvo:
            return iterador
        else:
            continue
    return "Alvo não encontrado!"


print(percorrerListaWhile(listinha, alvo=41))
