from abc import ABC, abstractmethod

class AnimalInterface(ABC):
    @abstractmethod
    def makeSound(self): pass
    #@abstractmethod
    #def canBark(self): pass

class Animal(AnimalInterface):
    def makeSound(self):
        print("Animal Sound!")

    def canClimb(self):
        print("Some animals can climb!")

class Dog(Animal):
    def makeSound(self):
        print("Woof woof!")

class Cat(Animal):
    def makeSound(self):
        print("Meow meow!")

    def canClimb(self):
        print("Cat can climb!")

#Animal().makeSound()
Dog().makeSound()
Cat().makeSound()
Dog().canClimb()
Cat().canClimb()

# Polymorphism
animals = [Dog(), Cat(), Cat()]
for a in animals:
    a.makeSound()
