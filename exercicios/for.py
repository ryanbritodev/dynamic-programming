###################################################
# Exercício N°3

lista = [10, 20, 30, 40, 50]

alvo = 30

for i, a in enumerate(lista):
    if a == alvo:
        print(f"O alvo está na posição {a}")
        break
else:
    print("Alvo não encontrado!")
