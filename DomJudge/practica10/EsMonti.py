import sys

def isHeap(H):
    for i in xrange(1, len(H)):
        if H[parent(i)] > H[i]:
            return False
    else:
        return True

def parent(i):
    return (i - 1) / 2

def read():
    while True:
        if int(sys.stdin.readline()) == 0:
            return
        line = sys.stdin.readline()
        hp = map(int, line.split())

        if isHeap(hp):
            print 'Yes'
        else:
            print 'No'

read()
