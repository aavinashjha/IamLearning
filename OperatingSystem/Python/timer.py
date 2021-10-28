"""
Timer is a subclass of Thread
- Action should be run after a certain amount of time has passed
- Could be cancelled if its waiting

class threading.Timer(interval, function, args=None, kwargs=None)
"""
from threading import Timer

def task():
    print("Thread is running...")

t = Timer(3.0, task)
t.start()
t.cancel()
