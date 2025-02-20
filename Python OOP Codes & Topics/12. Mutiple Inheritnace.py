class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Method1 of class A")

class B:

    def __init__(self):
        print("__init__ of class B")

    def method2(self):
        print("Method1 of class B")

class C(A,B):
    def __init__(self):
        #super().__init__() this will take only class A
        A.__init__(self) #but in this method we can take constructor of both A & B
        B.__init__(self)
        print("__init__ of class C")

    def method3(self):
        print("Method2 of class C")

obj = C()
obj.method1()
obj.method2()
obj.method3()
