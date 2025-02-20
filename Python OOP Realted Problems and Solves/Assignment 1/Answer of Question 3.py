class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

    def update(self,name,designation,num_of_wife,dictator):
        self.name = name
        self.designation = designation
        self.num_of_wife = num_of_wife
        self.dictator = dictator

    def details(self):
        print("Name of President:",self.name,
              "\nDesignation:",self.designation,
              "\nNumber of Wife:",self.num_of_wife,
              "\nIs He/She Dictator:",self.dictator)

#=============================================================

obj1 = Wadiya()
obj1.details()
print("======================================")
obj2 = Wadiya()
obj2.update("Donald Trump","President",1,"False")
obj2.details()