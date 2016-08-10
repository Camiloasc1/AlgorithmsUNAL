def rus(a, b):
    x, y, z = a, b, 0
    while x > 0:
        if x == 7:
            print y
        if x % 2 == 1:
            z += y
        y = y << 1
        x = x >> 1
    return z

print rus(63, 12)
