class House:
    def __init__(self,name):
        self.window = 4 # Here we are giving built in values for the all object (FIXED)
        self.door = 2
        self.name = name

    def view(self):
        print("This",self.name,"House has",self.window,"Windows",self.door,"Doors")

    def update_windows(self,window):
        self.window = window

    def update_doors(self,door):
        self.door = door
#============================================================================================
H1 = House("ShawpnoDhara")
H1.view()
print("====================")
print("After Manipulation by direct Instance Variable:")
print()
H1.window=32
H1.door=20
H1.view()
#===================================================================================
#Here updating the instance variable by calling the instance method
H1.update_windows(56)
H1.update_doors(28)
print("===================================")
print("By calling Instances Method by object to update the Values")
print("")
H1.view()
print(type(H1.door))
print(H1.__dict__)#it is showing all the instances name value by dictionary SHOWS THE UPDATED VALUE
print()
