import math

def isPrime(n):
    if n == 2:
        return True
    lim = int(math.ceil(math.sqrt(n))) + 1
    for i in xrange(3, lim, 2):
            if n % i == 0:
                return False
    return True

def run(a, b):
    if a % 2 == 0:
        a += 1
    for i in xrange(a, b + 1, 2):
        if isPrime(i):
            print i

n = input()

for i in xrange(n):
    a, b = raw_input().split()
    run(int(a), int(b))
