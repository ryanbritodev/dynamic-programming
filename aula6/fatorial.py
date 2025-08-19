# O que é Recursão?
# É uma técnica onde uma função chama a si mesma para resolver um
# problema, dividindo-o em subproblemas menores e mais simples. É
# como um ciclo onde a função se repete até atingir uma condição de
# parada.
# Uso: problemas naturalmente divisíveis em subproblemas menores :)

def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)

print(fat(995))
