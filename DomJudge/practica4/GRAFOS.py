import sys
import math

def grafos():
    data = sys.stdin.read().splitlines()
    for line in data:
        values = line.split()
        if values[0] == "chain":
            print int(values[1]) - 1
        elif values[0] == "ring":
            print int(values[1])
        elif values[0] == "grid":
            print int(2 * int(values[1]) - 2 * math.sqrt(int(values[1])))
        elif values[0] == "complete":
            print sum(xrange(int(values[1])))

grafos()
