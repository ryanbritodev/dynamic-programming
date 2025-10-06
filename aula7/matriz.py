def caminhos_unicos(m, n):
    """
    Calcula o número de caminhos únicos em uma grade m x n.

    Parâmetros:
    m (int): número de linhas da grade
    n (int): número de colunas da grade

    Retorna:
    int: número total de caminhos únicos
    """
    # Criar tabela de programação dinâmica
    tabela = [[0 for _ in range(n)] for _ in range(m)]

    # Caso base: ponto inicial
    tabela[0][0] = 1

    # Preencher a tabela usando tabulação (bottom-up)
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                # Já inicializado
                continue
            elif i == 0:
                # Primeira linha: só pode vir da esquerda
                tabela[i][j] = tabela[i][j - 1]
            elif j == 0:
                # Primeira coluna: só pode vir de cima
                tabela[i][j] = tabela[i - 1][j]
            else:
                # Relação de recorrência
                tabela[i][j] = tabela[i - 1][j] + tabela[i][j - 1]

    return tabela[m - 1][n - 1]


def visualizar_tabela(m, n):
    """
    Visualiza a tabela de programação dinâmica com os valores calculados.
    """
    tabela = [[0 for _ in range(n)] for _ in range(m)]
    tabela[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                tabela[i][j] = tabela[i][j - 1]
            elif j == 0:
                tabela[i][j] = tabela[i - 1][j]
            else:
                tabela[i][j] = tabela[i - 1][j] + tabela[i][j - 1]

    print(f"\nTabela DP para grade {m}x{n}:")
    print("-" * (6 * n))
    for i in range(m):
        linha = ""
        for j in range(n):
            linha += f"{tabela[i][j]:5} "
        print(linha)
    print("-" * (6 * n))
    print(f"Total de caminhos: {tabela[m - 1][n - 1]}\n")


# Exemplos de uso
if __name__ == "__main__":
    print("=" * 50)
    print("CAMINHOS ÚNICOS EM GRADE - PROGRAMAÇÃO DINÂMICA")
    print("=" * 50)

    # Teste 1: Grade 3x3 (exemplo do enunciado)
    print("\n📊 Teste 1: Grade 3x3")
    resultado = caminhos_unicos(3, 3)
    print(f"Caminhos únicos: {resultado}")
    visualizar_tabela(3, 3)

    # Teste 2: Grade 3x7
    print("📊 Teste 2: Grade 3x7")
    resultado = caminhos_unicos(3, 7)
    print(f"Caminhos únicos: {resultado}")
    visualizar_tabela(3, 7)

    # Teste 3: Grade 4x4
    print("📊 Teste 3: Grade 4x4")
    resultado = caminhos_unicos(4, 4)
    print(f"Caminhos únicos: {resultado}")
    visualizar_tabela(4, 4)

    # Teste 4: Grade 2x2 (caso simples)
    print("📊 Teste 4: Grade 2x2")
    resultado = caminhos_unicos(2, 2)
    print(f"Caminhos únicos: {resultado}")
    visualizar_tabela(2, 2)

    # Teste 5: Grade 1x5 (apenas uma linha)
    print("📊 Teste 5: Grade 1x5")
    resultado = caminhos_unicos(1, 5)
    print(f"Caminhos únicos: {resultado}")

    # Teste 6: Grade 5x1 (apenas uma coluna)
    print("📊 Teste 6: Grade 5x1")
    resultado = caminhos_unicos(5, 1)
    print(f"Caminhos únicos: {resultado}")

    print("\n" + "=" * 50)
    print("Complexidade:")
    print("  • Tempo: O(m × n)")
    print("  • Espaço: O(m × n)")
    print("=" * 50)