def potencia_bottom_up(a, b):
    if b == 0:
        return 1

    tabela = [0] * (b + 1)

    tabela[0] = 1

    for i in range(1, b + 1):
        tabela[i] = tabela[i - 1] * a

    return tabela[b]

for i in range(1, 10):
    print(potencia_bottom_up(i, 2))
