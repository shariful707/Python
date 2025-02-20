from abc import ABC, abstractmethod

class A:
    @abstractmethod
    def method1(self): #This kind of class has only declaration with no body or instance variables
        pass

class B(A):
    @abstractmethod
    def method2(self): #This kind of class has only declaration with no body or instance variables
        pass

class C(B):
    def method1(self): #if not override then wont create object
        print("This is method1 from Class A the grandparent or super base")
    def method2(self): #if not override then wont create object
        print("This is method2 from Class B the parent")
    def method3(self):
        print("This is method3 from Class C the child")

#Both case you have to override all abstract class in main class

obj = C()
obj.method1()
obj.method2()
obj.method3()