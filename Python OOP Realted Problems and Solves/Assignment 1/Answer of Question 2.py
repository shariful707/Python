from contextlib import nullcontext


class Flower:
    def __init__(self):
        self.name= None
        self.color = None
        self.num_of_petal=None




flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=======================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)
print("=============================")
print("Address of flower1",flower1)
print("Address of flower2",flower2)
