import time
import logging
import threading
"""
Daemon thread:
    - Main thread have to wait for everyone to finish
    - If daemon thread, we can kill main thread and others will be stopped automatically
"""
logging.basicConfig(level=logging.DEBUG,
        format='%(threadName)-9s : %(message)s',)

def tasknd():
    logging.debug("Starting thread")
    logging.debug("Ending thread")

def taskd():
    logging.debug("Starting thread")
    time.sleep(5)
    logging.debug("Ending thread")

logging.debug("Starting main thread")

t1 = threading.Thread(name="daemon", target=taskd)
# If we set thread as daemon, we will not wait for it to complete
# and main program will finish as it reaches end of floe
t1.setDaemon(True)

t2 = threading.Thread(name="non-daemon", target=tasknd)

t1.start()
t2.start()

main = threading.current_thread()
print("#########################")
# Enumerates all alive threads
for t in threading.enumerate():
    if t is main:
        print("Main thread: ", t.getName())
    else:
        print("Child thread: ", t.getName())
print("#########################")

# Join blocks indefinitely
#t1.join(timeout=6)
# Less timeout, hence thread would be still alive
t1.join(timeout=2)
if t1.isAlive():
    logging.debug("Daemon thread is still alive")
else:
    logging.debug("Daemon thread is dead")

logging.debug("Ending main thread")
