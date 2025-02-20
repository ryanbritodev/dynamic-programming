class Corrente:
    def __init__(self, pot: float = 0, volt: float = 0, res: float = 0, cor: float = 0):
        self.pot = pot
        self.volt = volt
        self.res = res
        self.cor = cor

    def calcularCorrente(self):
        if self.volt == 0:
            return 0
        return self.pot / self.volt

    def calcularVoltagem(self):
        return self.res * self.cor

    def calcularPotencia(self):
        return self.res * (self.cor**2)


estrutura = Corrente(pot=20, volt=110, res=5, cor=2)
corrente = estrutura.calcularCorrente()
potencia = estrutura.calcularPotencia()
voltagem = estrutura.calcularVoltagem()

print("Corrente: ", corrente)
print("Voltagem: ", voltagem)
print("Potência: ", potencia)
