def fatorial_bottom_up(n):
    if n == 0:
        return 1

    tabela = [0] * (n + 1)

    tabela[0] = 1

    for i in range(1, n + 1):
        tabela[i] = i * tabela[i - 1]

    return tabela[n]

for i in range(0, 6):
    print(fatorial_bottom_up(i))
