# Programa Equação Primeiro Grau
# ax + b = 0

class Equacao:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calcularEquacao(self):
        return -self.b / self.a


equacao = Equacao(1, 2)

print(equacao.calcularEquacao())
