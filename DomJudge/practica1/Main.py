from practica1.Generator import generateList
from practica1.Timer import Timer
from practica1.Sort import InsertionSort
from practica1.CheckSort import isSorted

avg = lambda x: (sum(x) / len(x))

timer = Timer()
times = [{}, {}, {}]
# time1 = dict.fromkeys([i for i in xrange(100, 1001, 100)],[])

print "n , time1 , time2 , time3"
for i in xrange(100, 1001, 100):
    if i not in times[0]:
        times[0][i] = []
        times[1][i] = []
        times[2][i] = []
    for _ in xrange(10):
        values = generateList(i)
        
        timer.start()
        InsertionSort(values[0])
        time = timer.stop()
        times[0][i].append(time)
        
        timer.start()
        InsertionSort(values[1])
        time = timer.stop()
        times[1][i].append(time)
        
        timer.start()
        InsertionSort(values[2])
        time = timer.stop()
        times[2][i].append(time)
    print i, ",", avg(times[0][i]), ",", avg(times[1][i]), ",", avg(times[2][i])

# print time1
