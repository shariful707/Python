from abc import ABC, abstractmethod

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name,"is Eating")

    @abstractmethod
    def action(self):
        pass

class Dog(Animal):
    def action(self):
        print(self.name,"is a dog which is Barking")

class Cat(Animal):
    def action(self):
        print(self.name,"is a cat which is Relaxing")

dog1 = Dog("Shawn")
cat1 = Cat("Piku")
dog1.action()
dog1.eat()
cat1.action()
cat1.eat()