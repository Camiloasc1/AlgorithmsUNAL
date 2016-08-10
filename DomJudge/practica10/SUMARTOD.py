import sys

def sumCost(nums):
    check = 0
    while len(nums) > 1:
        n1 = min(nums)
        nums.remove(n1)
        n2 = min(nums)
        nums.remove(n2)
        nums.append(n1 + n2)
        check += n1 + n2
    return check

def read():
    while True:
        if int(sys.stdin.readline()) == 0:
            return
        line = sys.stdin.readline()
        nums = map(int, line.split())

        print sumCost(nums)

read()
