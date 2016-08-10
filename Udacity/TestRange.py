import time

#use time.time() on Linux

start = time.time()
for x in range(10000000):
    pass
stop = time.time()

print stop - start

start = time.time()
for x in xrange(10000000):
    pass
stop = time.time()

print stop - start