
def isSorted(iterable):
    for i in xrange(len(iterable)-1):
        if iterable[i] > iterable[i+1]:
            return False
    else:
        return True