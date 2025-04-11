#Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):  # Abstract method (no body)
        pass

class Dog(Animal):
    def sound(self):
        print("Barks")

class Cat(Animal):
    def sound(self):
        print("Meows")

# Trying to instantiate Animal directly will raise an error
# animal = Animal()  ❌ Error

d = Dog()
c = Cat()
d.sound()  # Barks
c.sound()  # Meows
