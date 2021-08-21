"""
Abstract Factory Pattern:
    It is like factory pattern, but everything is encapsulated
    > The method that orders the object
    > The factories that build the object
    > The final objects
    > The final objects contain objects that use the Startegy pattern

What can you do with Abstract Factory Pattern?
- Allows you to create families of related objects without specifying a concete class
- Use when you have many objects that can be added or changed dynamically during runtime

Define generic ordering form (salesman)

"""
from abc import ABC, abstractmethod

class EnemyShipBuilding(ABC):
    def makeEnemyShip(self, typeOfShip):

class EnemyShipTesting:
    def main(self):
        makeUFOs = UFOEnemyShipBuilding()
        makeUFOs.orderTheShip("UFO")
