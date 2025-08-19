def busca(lista, alvo):
    if len(lista) == 1:
        return True
    else:
       return lista[0] + busca(lista[alvo:])

lista = [1, 2, 3, 4, 5]

print(busca(lista, 2))
