import heapq

lista = [8, 3, 5, 7, 9, 4, 10]

n = 5

menores = heapq.nsmallest(n, lista)
maiores = heapq.nlargest(n, lista)

print(menores)
print(maiores)


dicionario = {
    "A": ["B", "C"],
    "B": ["A", "C", "D", "E"],
    "C": ["A", "B", "D"],
    "D": ["D", "C", "E"],
    "E": ["B", "D"]
}


caminhos_dict = set(dicionario["C"])
caminhos_dict2 = set(dicionario["E"])

caminhos_em_comum = caminhos_dict & caminhos_dict2

print(caminhos_em_comum)

caminhos_diferentes = caminhos_dict - caminhos_dict2

print(caminhos_diferentes)
