class Panda:

    def __init__(self,name, sex, age):
        self.name = name
        self.gender = sex
        self.age = age

    def sleep(self,hours = None):
        self.hours = hours
        if self.hours == None:
            return "{} duration is unknown thus can have only Bamboo leaves".format(self.name)
        elif self.hours >= 3 or self.hours <= 5:
            return "{} sleeps {} hours daily and have Mixed Veggies".format(self.name,self.hours)
        elif self.hours>= 6 or self.hours<= 8:
            return "{} sleeps {} hours daily and have Eggplant & Tofu".format(self.name, self.hours)
        elif self.hours>= 9 or self.hours<= 11:
            return "{} sleeps {} hours daily and have Broccoli & Chicken".format(self.name, self.hours)

panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())