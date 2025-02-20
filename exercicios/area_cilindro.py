import math


def calcula_volume_retangulo(base, altura, largura):
    return base * altura * largura


def calcula_area_retangulo(base, altura):
    return base * altura


def calcula_area_cilindro(raio, altura):
    return 2 * math.pi * raio * (raio + altura)


def calcula_volume_cilindro(raio, altura):
    return math.pi * (raio**2) * altura


menu = """1............ Cilindro
2............ Retângulo"""

while True:
    print(menu)
    opcao = str(input("Selecione sua opção [1 ou 2]: ")).strip()
    if opcao == "1":
        raioCilindro = float(input("Informe o raio: "))
        alturaCilindro = float(input("Informe a altura: "))
        print(f"Volume: {calcula_volume_cilindro(raioCilindro, alturaCilindro)}")
        print(f"Área: {calcula_area_cilindro(raioCilindro, alturaCilindro)}")
        break
    elif opcao == "2":
        baseRetangulo = float(input("Informe o raio: "))
        alturaRetangulo = float(input("Informe a altura: "))
        larguraRetangulo = float(input("Informe a largura: "))
        print(f"Volume: {calcula_volume_retangulo(baseRetangulo, alturaRetangulo, larguraRetangulo)}")
        print(f"Área: {calcula_area_retangulo(baseRetangulo, alturaRetangulo)}")
        break
    else:
        print("Opção inválida! Tente novamente ❌")

