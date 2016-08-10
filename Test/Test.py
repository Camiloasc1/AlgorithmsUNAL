import math

def isPrime(n):
    if n == 2:
        return True
    for i in xrange(3, int(math.ceil(math.sqrt(n))) + 1, 2):
            if n % i == 0:
                return False
    return True

print isPrime(1013669231)

def misterio(n):
    if n <= 1:
        return 0
    c=0
    i=1
    while i <= 5:
        i=i+1
        misterio(n/2)
        for j in range (1,n):
            for k in range (1,j):
                c+=1
    return c
print misterio(5)