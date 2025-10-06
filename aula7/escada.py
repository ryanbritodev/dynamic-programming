def subir_escadas(n):
    """
    Casos Base:
        tabela[0] = 1 (uma maneira, se estiver no chão)
        tabela[1] = 1 (uma maneira de chegar ao primeiro degrau
    Relação de recorrência:
        tabela[i] = tabela[i - 1] + tabela[i - 2]
    """
    if n == 0 or n == 1:
        return 1

    tabela = [0] *  (n + 1)

    tabela[0] = 1
    tabela[1] = 1

    for i in range(2, n + 1):                                                                                                                                                                                                                                                                                           
        tabela[i] = tabela[i - 1] + tabela[i - 2]

    return  tabela[n]

print(f"Para 5 degraus, existem {subir_escadas(5)} maneiras.")
print(f"Para 10 degraus, existem {subir_escadas(10)} maneiras.")
print(f"Para 20 degraus, existem {subir_escadas(20)} maneiras.", end="")
