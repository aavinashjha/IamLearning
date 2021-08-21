"""
Problem:
    - Who should be responsible for creating objects when there are special
      considerations such as complex creation logic, a desire to separate
      the creation responsibilites for better cohesion?

When you need a factory pattern?
- When you don't know ahead of time what class object you need
- When all the potential classes are in same subclass hierarchy
- To centralize class selection code
- When you don't want the user to have to know every subclass
- To encapsulate object creation

Solution:
- Create a Pure Fabrication object called factory that handles the creation

NOTES:
- When a method returns one of several possible classes that share a common super class
  > Create a new enemy in game
  > Random number generator picks a number assigned to a specific enemy
  > The factory returns the enemy associated with that number
  > Class is chosen at runtime

Client -> EnemyShipFactory -> EnemyShip (Implemented by UFOEnemyShip, RocketEnemyShip)\
The Factory Pattern allows you to create objects without specifying the exact class of object
that will be created.
"""
from abc import ABC, abstractmethod
class EnemyShip(ABC):

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDamage(self):
        return self.damage

    def setDamage(self, damage):
        self.damage = damage

    def followHeroShip(self):
        print("{} is following the hero".format(self.getName()))

    def displayEnemyShip(self):
        print("{} is on the screen".format(self.getName()))

    def enemyShipShoots(self):
        print("{} attacks and does {}".format(self.getName(), self.getDamage()))

class UFOEnemyShip(EnemyShip):
    def __init__(self):
        self.setName("UFO Enemy Ship")
        self.setDamage(20)
    

class RocketEnemyShip(EnemyShip):
    def __init__(self):
        self.setName("Rocket Enemy Ship")
        self.setDamage(10)

class BigEnemyShip(EnemyShip):
    def __init__(self):
        self.setName("Big Enemy Ship")
        self.setDamage(40)

class EnemyShipFactory:

    def makeEnemyShip(self, shipType):
        enemy = None
        if shipType == "U": enemy = UFOEnemyShip()
        elif shipType == "R": enemy = RocketEnemyShip()
        elif shipType == "B": enemy = BigEnemyShip()
        return enemy

def doStuffEnemy(enemyShip):
    enemyShip.displayEnemyShip()
    enemyShip.followHeroShip()
    enemyShip.enemyShipShoots()


shipFactory = EnemyShipFactory()
while True:
    shipType = input("Which ship you want: U/R/B")
    enemy = shipFactory.makeEnemyShip(shipType)
    doStuffEnemy(enemy)
# This bunch of if else is bad, we have a better way by using factory pattern
"""
while True:
    shipType = input("Which ship you want: U/R")
    enemy = None
    if shipType == "U":
        enemy = UFOEnemyShip()
    if shipType == "R":
        enemy = RocketEnemyShip()
    doStuffEnemy(enemy)
"""
