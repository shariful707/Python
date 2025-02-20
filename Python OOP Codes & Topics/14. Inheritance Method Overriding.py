class A:
    def __init__(self,name):
        self.name = name

    def method1(self):
        print(self.name,'read More!')

class B(A):

    def method1(self):
        A.method1(self)

        print(self.name,"Have party")


#==================================================
p1 = B("Anim")
p1.method1()