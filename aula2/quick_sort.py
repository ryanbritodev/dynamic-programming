lista = [10, 80, 30, 90, 40, 50, 70]


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    menores = [x for x in lista[:-1] if x <= pivo]
    maiores = [x for x in lista[:-1] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


print("Lista ordenada: ", quick_sort(lista))
