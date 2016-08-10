import sys

def check(board):
    pass

boards = sys.stdin.read().splitlines()
for b in boards:
    if check(b):
        print 'valid'
    else:
        print 'invalid'