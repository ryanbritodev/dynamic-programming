def busca_linear(lista, alvo):
   if len(lista) == 0:
      return False
   elif lista[0] == alvo:
      return True
   else:
      lista.pop(0)
      return busca_linear(lista, alvo)

listinha = [1, 2, 3]

print(busca_linear(listinha, 1))
