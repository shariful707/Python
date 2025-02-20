#Single Inheritance means 1 parent 1 class
class Animal: #This is Parent class

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name,"is eating")
#========================================================================
class Dog(Animal): #This is Child class
    def bark(self): #here we do not define __init__ or constructor because it has inherited it from parent Class Animal but can define if we use more instances or variables
        print(self.name,"is a Dog which is Barking!")
#==============================================================================
dog1 = Dog('Shawn')
dog1.eat()
dog1.bark()
print('=====================')
dog2= Animal("lucy")
dog2.eat()
#dog2.bark() # here it will not work because we created dog2 object from only Animal and it will access Animal class's methods not the Dog Class's methods.
