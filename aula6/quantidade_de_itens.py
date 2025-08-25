listinha = [1, 1, 2, 2, 3, 3]

def contador(lista, item):
    if len(lista) == 0:
        return 0
    elif lista[0] == item:
        return 1 + contador(lista, item)
    else:
        return 0 + contador(lista, item)
