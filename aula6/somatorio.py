def somatorio(n):
    if n == 0:
        return 0
    else:
        return n + somatorio(n - 1)

print(somatorio(3))
