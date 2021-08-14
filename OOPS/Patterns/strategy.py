"""
Problem:
    How to design for varying but related algorithms?
    How to design for the ability to change these algorithms or policies?
Solution:
    Define each algorithm/policy/strategy in a separate class with a common interface
When to use strategy pattern:
    When you want to define a class that will have one behavior that is similar to other behaviors in a list
    I want the class object to choose from
    - Not flying
    - Fly with wings
    - Fly Super Fast
    When you need to use one of several behaviors dynamically
    Often reduces long list of conditionals
    Avoids duplicate code
    Keeps class changes from forcing other class changes
    Can hide complicated/ secret code from user
    Negative: Increased number of classes/objects
NOTES:
    - The interface for the strategy object must accept as a parameter a reference of the context object
    - A strategy object is used only by one context object (DontFly is used by Dog)
    - When a context object sends a message to the strategy object a reference of the context object must be
      passed as a parameter for further collaboration
    - Dog sends a message to DontFly strategy for further collaboration - parameter visibility
    - The context object must use as a reference to the strategy interface to send messages

Idea1: Add fly in superclass
We don't want to add functionality in super class which doesn't pertains to any subclass
Like Bird and Giraffe are subclass and Animal is superclass, so we shouldn't add fly in animal superclass.
This would be bad code.

Idea2: Use interface to force the creation of a method
Avoid interfaces that just force action
Using an interface just to force the creation of a method is a bad idea

- Avoid duplicate code
- Change in superclass or subclass shouldn't break anything

 +++++++++++++++++++     +++++++++++++++++++
 + Animal          +hasA + <interface> Fly +
 +                 +---> +                 +
 +++++++++++++++++++     +++++++++++++++++++
                         + +fly(): String  +
                         +                 +
                         +++++++++++++++++++

                             ^
                             ! Implements
                             !
            +++++++++++++++++++     +++++++++++++++++++
            + DoesFly         +     + DontFly         +
            +                 +     +                 +
            +++++++++++++++++++     +++++++++++++++++++
            + +fly(): String  +     + +fly(): String  +
            +                 +     +                 +
            +++++++++++++++++++     +++++++++++++++++++

Define a family of algorithms(strategies), encapsulate each one, and make them interchangeable.(DoesFly, DontFly)
The strategy pattern lets the algorithm vary independently from clients that use it.

Another example:
    Client: Provides algorithm to Context
    Context: Uses abstract interface to algorithm
    SortStrategy is interface
    Implementations: Bubble, Selection, Merge, Quick
    Adding new algorithms doesn't impact context
"""
from abc import ABC, abstractmethod

class Fly(ABC):
    @abstractmethod
    def fly(self):
        pass

class DoesFly(Fly):
    def fly(self):
        return "It can fly!"

class DontFly(Fly):
    def fly(self):
        return "It doesn't fly!"


class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass
    @abstractmethod
    def fly(self):
        pass


class Dog(Animal):
    def __init__(self):
        self.flyingType = DontFly()

    def makeSound(self):
        return "Woof woof!"

    def fly(self):
        return self.flyingType.fly()

class Cat(Animal):
    def __init__(self):
        self.flyingType = DontFly()

    def makeSound(self):
        return "Meow meow!"
    def fly(self):
        return self.flyingType.fly()

class Bird(Animal):
    def __init__(self):
        self.flyingType = DoesFly()

    def makeSound(self):
        return "Chirp chirp!"
    def fly(self):
        return self.flyingType.fly()

animals = [Dog(), Bird(), Cat()]
for a in animals:
    print("{} do {}. {}".format(type(a).__name__, a.makeSound(), a.fly()))
