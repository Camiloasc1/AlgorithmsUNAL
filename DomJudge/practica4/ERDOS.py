import sys
import math

def binomial(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

def binomial2(n):
    return int(n*(n-1)/(2))

def erdos():
    data = sys.stdin.read().splitlines()
    for l in data:
        line = l.split()
        print int(binomial2(int(line[0])) * float(line[1]))
    
erdos()
