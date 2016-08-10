def count(string):
    check = {}
    for c in string:
        if c not in check:
            check[c] = 0
        check[c] += 1
    return check

for _ in xrange(int(raw_input())):
    strings = raw_input().split()
    if count(strings[0]) == count(strings[1]):
        print 'true'
    else:
        print 'false'
