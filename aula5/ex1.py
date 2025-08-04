pessoa = []
lista_pessoa = []
contador = 0

while contador < 2:
    print(f"\nDados da {contador + 1} pessoa: ")
    nome = input("Digite o nome: ")
    pessoa.append(nome)
    idade = int(input("Digite a idade: "))
    pessoa.append(idade)
    sexo = input("Digite o sexo da pessoa: ")
    pessoa.append(sexo)
    lista_pessoa.append(pessoa)
    pessoa = []
    contador += 1
    
print(f"\nLista de pessoas: {lista_pessoa}")
