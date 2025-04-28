import heapq

lista = [8, 3, 5, 7, 9, 4, 10]

n = 5

menores = heapq.nsmallest(n, lista)
maiores = heapq.nlargest(n, lista)

print(menores)
print(maiores)
