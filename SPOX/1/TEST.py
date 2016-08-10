import sys
nums = map(int, sys.stdin.read().splitlines())
print "\n".join(map(str, nums[:nums.index(42)]))
