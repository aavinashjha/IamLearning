"""
Thread class represents an activity that runs in separate thread of control
- By passing callable object to constructor
- By overriding run method in subclass

Override just __init__ and run methods of a class
"""
import time
import logging
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
        format='%(threadName)-9s %(message)s',)

class NewThread(Thread):
    def __init__(self, args=(), kwargs={}):
        super().__init__(args=args, kwargs=kwargs)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("Waiting in run of new thread: {}: {}".format(self.args, self.kwargs))
        time.sleep(5)

t = NewThread(args=("Hello there",), kwargs={"a":1})
t.start()
logging.debug("Child Alive: {}".format(t.isAlive()))

