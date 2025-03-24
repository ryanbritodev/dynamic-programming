# Exercício 2
# Uma impressora recebe pedidos de impressão de diferentes usuários. Cada documento
# tem um nome e um nível de prioridade (alta ou baixa). Os documentos de prioridade alta devem
# ser impressos antes dos de prioridade baixa.

lista_baixa_prioridade = []
lista_alta_prioridade = []

menu = """\n##### FILA DE DOCUMENTOS #####
1. Adicionar documento de alta prioridade
2. Adicionar documento de baixa prioridade
3. Sair da estrutura\n"""

while True:
    try:
        print(menu)
        lista_impressao = []

        if not lista_alta_prioridade and not lista_baixa_prioridade:
            pass
        elif lista_alta_prioridade and lista_baixa_prioridade:
            for i in lista_alta_prioridade:
                lista_impressao.append(i)
            for j in lista_baixa_prioridade:
                lista_impressao.append(j)
        elif lista_alta_prioridade and not lista_baixa_prioridade:
            for i in lista_alta_prioridade:
                lista_impressao.append(i)
        elif lista_baixa_prioridade and not lista_alta_prioridade:
            for j in lista_baixa_prioridade:
                lista_impressao.append(j)

        print(f"Fila atual: {lista_impressao}")
        opcao = int(input("Escolha sua opção: "))
        match opcao:
            case 1:
                nome_documento = str(input("\nInforme o nome do documento de alta prioridade: "))
                lista_alta_prioridade.append(nome_documento)
            case 2:
                nome_documento = str(input("\nInforme o nome do documento de baixa prioridade: "))
                lista_baixa_prioridade.append(nome_documento)
            case 3:
                print("\nSaindo da estrutura...")
                print(f"Fila final: {lista_impressao}")
                break
            case _:
                print("Opção inválida! Tente novamente")

    except ValueError:
        print("\nNúmero inválido! Tente novamente")
        continue
