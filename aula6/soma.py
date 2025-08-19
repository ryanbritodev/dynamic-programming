def somatorio(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somatorio(lista[1:])

lista1 = [1, 3, 5, 7, 9, 2, 2]

print(somatorio(lista1))
