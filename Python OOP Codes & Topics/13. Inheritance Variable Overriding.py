class Animal:
    
    def __init__(self,name):
        self.name = name
        self.color = "White"
        
    def eat(self):
        print(self.color,self.name,"is Eating")
        
class Dog(Animal):
    
    def __init__(self,name,color):
        super().__init__(name) #Here omittsing the color for overriding
        self.color = color # Here we are overriding the value of parent's instance variable's

    def bark(self):
        print(self.color, self.name, 'is Barking')

#========================================================================

d1 = Dog("Shawn","Red")
d1.eat()
d1.bark()