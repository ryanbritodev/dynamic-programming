# Crie uma estrutura para solicitar o clima para o usuário: ensolarado, chuvoso, nublado, ensolarado.

clima = str(input("Informe o clima atual: ")).strip().upper()

if clima == "ENSOLARADO":
    print("Dia de Futebol e Churrasco! 🍖⚽")
elif clima == "CHUVOSO":
    print("Dia de Filme e Série! 📽️🎬")
elif clima == "NUBLADO":
    print("Dia de Ler um Livro! 📖")
elif clima == "NEVANDO":
    print("Dia de Tomar um Café! ☕")
else:
    print("Dia Inválido! ❌")
