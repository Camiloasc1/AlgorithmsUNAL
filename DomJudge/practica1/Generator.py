import random

def generateList(lon):
    values = [[i for i in xrange(1,lon+1)],[i for i in xrange(lon,0,-1)],[i for i in xrange(1,lon+1)]]
    random.shuffle(values[2])
    return values

print generateList(5)