import logging
import threading
"""
Thread constructor
def __init__(self, group=None, target=None, name=None,
             args=(), kwargs=None, *, daemon=None):

RuntimeError: If same thread object is called twice
run methid is called by start method

Daemon thread:
    - Main thread have to wait for everyone to finish
    - If daemon thread, we can kill main thread and others will be stopped automatically
"""
logging.basicConfig(level=logging.DEBUG,
        format='%(levelname)s %(threadName)-9s %(message)s',)

def task(num):
    logging.debug("{}: Hello from task {}!".format(threading.currentThread().getName(), num))

for i in range(11):
    t = threading.Thread(name= 'Thread {}'.format(i), target=task, args=(i, ))
    t.start()

