class Customer:

    def __init__(self,name):
        self.name = name
        print("Hello!")

    def greet(self):
        print("Greetings",self.name,"!",
              "\nYou have purchased",self.num_of_item,"Item(s)")

    def purchase(self,*items):
        self.num_of_item = len(items)
        self.greet()
        for x in items:
            print(x)

buyer1 = Customer("SAM")
buyer1.purchase("Tomato","Chip","Coke")

