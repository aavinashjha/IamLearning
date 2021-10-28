"""
Constraints:
    - One of the simplest mechanism for communicating between threads
    - One thread signals an event and other thread waits for it
"""
import time
from threading import Thread, Event

def task_notimeout(e):
    print("waiting indefinitely")
    e.wait()
    print('exiting notimeout')

def task_timeout(e, t):
    print("waiting for {} seconds".format(t))
    e.wait(t)
    print('exiting timeout')

e = Event()
notimeout = Thread(target=task_notimeout, args=(e,))
timeout = Thread(target=task_timeout, args=(e, 2.0,))

notimeout.start()
timeout.start()

time.sleep(5)
e.set()
