def mdc(x, y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return mdc(y, x)
    else:
        return mdc(y, x % y)

print(mdc(10, 5))
