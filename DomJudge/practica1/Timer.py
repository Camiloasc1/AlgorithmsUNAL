import time

#use time.time() on Linux

class Timer(object):
    def __init__(self):
        self.time = 0
        self.isStarted = False
        
    def start(self):
        self.isStarted = True
        self.time = time.time()
    
    def stop(self):
        if self.isStarted:
            self.isStarted = False
            return time.time() - self.time
        return 0 
