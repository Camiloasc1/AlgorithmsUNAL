
def InsertionSort(iterable):
    for i in xrange(1,len(iterable)):
        j = i
        while j > 0 and iterable[j] < iterable[j-1]:
            iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
            j -= 1
    return iterable