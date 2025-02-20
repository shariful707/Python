class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("Speaking as Class A")

class Cat(Animal):

    def speak(self): #It has defines in Parent class
        print("Meow")

class Dog(Animal):

    def speak(self): #It has defines in Parent class
        print("Woo Woo")


obj1 = Cat()
obj2 = Dog()
obj1.speak() # But it is calling the child class's method
obj2.speak() # But it is calling the child class's method


#This is called polymorphism while i have a shape of a method in PARENT but still I change it as per my need in CHILD or any where else
#Basically method overriding and overloadding is Polymorphism