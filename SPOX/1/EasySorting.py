for _ in xrange(int(raw_input())):
    strings = []
    for _ in xrange(int(raw_input())):
        strings.append(raw_input())

    print "\n".join(sorted(strings))
