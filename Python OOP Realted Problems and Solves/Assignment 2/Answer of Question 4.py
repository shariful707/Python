class Cat:
    def __init__(self,*var):
        if len(var)==0:
            self.color = "White"
            self.action = "Sitting"
        elif len(var)==1:
            self.color = var[0]
            self.action = "Sitting"
        elif len(var) == 2:
            self.color = var[0]
            self.action = var[1]

    def changeColor(self,color):
        self.color = color

    def printCat(self):
        print(self.color,"cat is",self.action)


c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()