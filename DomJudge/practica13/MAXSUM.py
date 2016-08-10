import sys

def solve(nums):
    if len(nums) == 1:
        return nums[0]
    M = 0
    for l in xrange(len(nums)):
        M = max(M, solve2(nums[l:]))
    return M

def solve2(nums):
    if len(nums) == 1:
        return nums[0]
    M = 0
    for l in xrange(len(nums)):
        M = max(M, sum(nums[:l + 1]))
    return M

def read():
    for l in sys.stdin.read().splitlines():
        nums = map(int, l.split())
        print solve(nums)
read()
