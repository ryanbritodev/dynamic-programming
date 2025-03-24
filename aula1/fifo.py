# Exercício 1
# Criar uma estrutura a qual o número 1 seja possível adicionar documentos, 2 seja possível
# retirar os documentos da fila, 3 sair da estrutura da FIFO.

lista_documentos = []

menu = """\n##### FILA DE DOCUMENTOS #####
1. Adicionar documentos na lista
2. Retirar documentos da lista
3. Sair da estrutura FIFO\n"""

while True:
    try:
        print(menu)
        print(f"Fila atual: {lista_documentos}")
        opcao = int(input("Escolha sua opção: "))
        match opcao:
            case 1:
                nome_documento = str(input("\nInforme o nome do documento: "))
                lista_documentos.append(nome_documento)
            case 2:
                while True:
                    if lista_documentos:
                        print(f"\nRetirando documento: {lista_documentos[0]}")
                        lista_documentos.pop(0)
                        break
                    else:
                        print("\nErro! Sua fila está vazia")
                        break
            case 3:
                print("\nSaindo da estrutura FIFO...")
                print(f"Fila final: {lista_documentos}")
                break
            case _:
                print("Opção inválida! Tente novamente")
    except ValueError:
        print("Número inválido! Tente novamente")
        continue
