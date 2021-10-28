import logging
from threading import Thread, Lock

logging.basicConfig(level=logging.DEBUG,
        format='%(threadName)-9s %(message)s',)
def worker(lock):
    logging.debug("Acquire")
    lock.acquire()
    logging.debug("Running")
    lock.release()
    logging.debug("Release")

lock = Lock()
for i in range(10):
    t = Thread(name='T{}'.format(i), target=worker, args=(lock,))
    t.start()
