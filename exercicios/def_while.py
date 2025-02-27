###################################################
# Exercício N°5

listinha = [10, 20, 30, 40, 50]


def percorrerListaWhile(lista, alvo):
    iterador = 0
    while iterador < len(lista):
        if lista[iterador] == alvo:
            return iterador
        iterador += 1
    return "Alvo não encontrado!"


print(percorrerListaWhile(listinha, alvo=32))
