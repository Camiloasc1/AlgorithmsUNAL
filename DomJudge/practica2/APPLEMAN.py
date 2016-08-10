import sys

def isO(x, y, board):
    if x < 0 or x >= len(board):
        return False
    if y < 0 or y >= len(board[x]):
        return False
    return board[x][y] == 'o'

def count(x, y, board):
    count = 0
    if isO(x - 1, y, board):
        count += 1
    if isO(x + 1, y, board):
        count += 1
    if isO(x, y - 1, board):
        count += 1
    if isO(x, y + 1, board):
        count += 1
    return count

n = int(raw_input())
while n != 0:
    board = []
    for _ in xrange(n):
        board.append(sys.stdin.readline())
    
    check = "YES"
    for x in xrange(n):
        for y in xrange(n):
            if count(x, y, board) % 2 != 0:
                check = "NO"
                break
    
    print check
    
    n = int(raw_input())
