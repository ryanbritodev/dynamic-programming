def potencia(a, b):
    if a ** b == 1:
        return 1
    else:
        return a * potencia(a, (b - 1))

print(potencia(4, 5))
