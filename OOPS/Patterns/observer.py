"""
Observer/Delegation Event/Publish Subscribe Pattern
Problem: Different kinds of subscriber objects are interested in the state changes
or events of a publisher object and want ot read in their own unique way when the
publisher generates an event.
Moreover, the publisher wants to maintain low coupling to the subscribers. What to do?

When to use the Observer Pattern?
 - When you need many other objects to receive an object when another object changes
 - Loose coupling is a benefit (The Subject(publisher) doesn't need to know anything about the Observer(subscriber))
 - Negatives: The Subject(publisher) may send updates that don't matter to the Observer(subscriber)
Solution:
    - Define a subscriber or listener interface
    - Subscribers implement this interface
    - The publisher can dynamically register subscribers who are interseted in an event
      and notify them when an event occurs
    - One publisher can have many subscribers for an event
    - When different objects may be interested in the events of changes in an object,
      which does not want to couple too tightly with them
    - Act as the publisher and allow other objects to subscribe to event, and notify them
      if here is a subscription
NOTES:
    - The observer pattern is a software design pattern in which an object, called the subject,
      maintains a list of dependents, called observers, and notifies them automatically of any
      state changes, usually by calling one of their methods
"""
import time
import random
import threading
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register(observer): pass
    @abstractmethod
    def unregister(observer): pass
    @abstractmethod
    def notifyObserver(): pass

class Observer(ABC):
    @abstractmethod
    def update(ibmPrice, applePrice, googlePrice): pass

class StockGrabber(Subject):
    def __init__(self):
        self.observers = list()
        self.ibmPrice = 0
        self.applePrice = 0
        self.googlePrice = 0

    def register(self, newObserver):
        print("Registered {} observer".format(len(self.observers)+1))
        self.observers.append(newObserver)

    def unregister(self, deleteObserver):
        index = self.observers.index(deleteObserver)
        del self.observers[index]
        print("Unregistered: {} observer".format(index+1))

    def notifyObserver(self):
        for o in self.observers:
            o.update(self.ibmPrice, self.applePrice, self.googlePrice)

    def setIBMPrice(self, newIBMPrice):
        self.ibmPrice = newIBMPrice
        self.notifyObserver()

    def setApplePrice(self, newApplePrice):
        self.applePrice = newApplePrice
        self.notifyObserver()

    def setGooglePrice(self, newGooglePrice):
        self.googlePrice = newGooglePrice
        self.notifyObserver()

class StockObserver(Observer):
    observerCount = 0
    def __init__(self, stockGrabber):
        self.stockGrabber = stockGrabber
        StockObserver.observerCount += 1
        self.observerID = StockObserver.observerCount
        stockGrabber.register(self)

    def update(self, ibmPrice, applePrice, googlePrice):
        self.ibmPrice = ibmPrice
        self.applePrice = applePrice
        self.googlePrice = googlePrice
        print("ObserverID: {}, IBM: {}, Apple: {}, Google: {}".\
                format(self.observerID, self.ibmPrice, self.applePrice, self.googlePrice))

def getStock(stockGrabber, waitTime, firm, baseValue):
    for i in range(20):
        time.sleep(waitTime)
        baseValue += random.uniform(-10, 10)

        if firm == "IBM": stockGrabber.setIBMPrice(baseValue)
        elif firm == "APPLE": stockGrabber.setApplePrice(baseValue)
        elif firm == "GOOGLE": stockGrabber.setGooglePrice(baseValue)

stockGrabber = StockGrabber()
observer1 = StockObserver(stockGrabber)
stockGrabber.setIBMPrice(200)
stockGrabber.setApplePrice(300)
stockGrabber.setGooglePrice(400)

observer2 = StockObserver(stockGrabber)
stockGrabber.setIBMPrice(250)
stockGrabber.setApplePrice(350)
stockGrabber.setGooglePrice(450)

stockGrabber.unregister(observer1)
stockGrabber.setIBMPrice(220)
stockGrabber.setApplePrice(320)
stockGrabber.setGooglePrice(420)

"""
stockGrabber.unregister(observer2)
stockGrabber.setIBMPrice(200)
stockGrabber.setApplePrice(300)
stockGrabber.setGooglePrice(400)
"""
ibmStock = threading.Thread(target=getStock, args=[stockGrabber, 2, "IBM", 100])
appleStock = threading.Thread(target=getStock, args=[stockGrabber, 2, "APPLE", 200])
googleStock = threading.Thread(target=getStock, args=[stockGrabber, 2, "GOOGLE", 300])
ibmStock.start()
appleStock.start()
googleStock.start()
