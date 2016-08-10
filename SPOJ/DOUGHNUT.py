def run(a, b, c):
    if b >= a * c:
        print 'yes'
    else:
        print 'no'

n = input()

for i in xrange(n):
    a, b, c = raw_input().split()
    run(int(a), int(b), int(c))
