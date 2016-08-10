def naive(a, b):
    x, y, z = a, b, 0
    while x > 0:
        if x == 20:
            print z
        z += y
        x -= 1
    return z

naive(63,12)