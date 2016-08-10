import random
import sys
import timeit


def generate():
    f = open("sample.txt", "w")
    lineno = random.randint(0, 1000000)
    divisor = random.randint(0, 10000000)
    f.write(str(lineno) + " " + str(divisor) + "\n")
    for _ in xrange(lineno):
        f.write(str(random.randint(0, 1000000000)) + "\n")
    f.close()

def read1():
    for l in sys.stdin.readlines(): # ~ 4,7
        print l

def read2():
    for l in sys.stdin.read().splitlines(): # ~ 4,2 Faster
        print l

# generate()
print timeit.timeit(read1)

