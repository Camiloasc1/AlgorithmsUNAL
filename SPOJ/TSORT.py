import sys

n = input()
data = sys.stdin.read().splitlines()

sortedList = []

for i in data:
    sortedList.append(int(i))
    
sortedList.sort()

for i in sortedList:
    print i

# V2

import sys

m = int(1E6 + 1)
count = [0] * m

n = int(raw_input())
for _ in xrange(n):
    count[int(sys.stdin.readline())] += 1

for i in xrange(m):
    # if(count[i]>0):
    #    print "\n".join(map(str, [i] * count[i]))
    for _ in xrange(count[i]):
        print i

# V3

import sys
raw_input()
print "\n".join(map(str, sorted(map(int, sys.stdin.read().splitlines()))))
