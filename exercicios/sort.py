lista = [5, 2, 9, 1, 5, 6]

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista2 = [5, 2, 9, 1, 5, 6]
lista_ordenada = sorted(lista2)
print(lista_ordenada)

lista3 = [5, 2, 9, 1, 5, 6]
lista_ordenada2 = sorted(lista, reverse=True)
print(lista_ordenada2)

lista4 = [('maca', 3), ('banana', 1),
          ('laranja', 2), ('uva', 1)]

# Ordenando pelos números com chave lambda usando a função sorted
lista_ordenada3 = sorted(lista4, key=lambda x: x[1])
print(lista_ordenada3)


lista5 = [('maca', 3, 100), ('banana', 1, 152),
          ('laranja', 2, 234), ('uva', 1, 135)]

lista_ordenada4 = sorted(lista5, key=lambda z: (z[1], z[0]))
print(lista_ordenada4)
