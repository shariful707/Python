class Employee: #Here this is declaring class name which is 'Employee'

    def __init__(self,name, age,dept,phone_num,address): #This is constructor with name parameter which can be used as instance variable
        self.name = name #Here self takes the reference value of the object/instance number that stored in the RAM
        self.age = age # here declaring instance variable not required in order
        self.dept = dept
        self.phone_num = phone_num
        self.address = address
        print("The Employee name is",self.name)

    def Info(self): #This is Instance Method
        print(self.name,'is',self.age,'years old')
        print(self.name, 'is from', self.dept, 'Department')
        print("Call",self.phone_num,"to reach",self.name)
        print("His Address:",self.address)

Employee1= Employee("Mohammad Shariful Alam Mollah",25,"Software Development",88001315770842,"Taqwa Tower, Mollah Para, Adarsha Nagar,Middle Badda, Dhaka-1212") #Employee1 is the object that is created from Employee class with name variable
Employee1.Info()
print("=============================")
print("Created Object's reference value or RAM slot",Employee1) #It prints the RAM location or the reference value of the created object

print("===============================")
print('Before Changing The age of the Employee1 object is',Employee1.age) #25
Employee1.age = 22  # We can change the instance variables value outside of the class
print('After Changing The age of the Employee1 object is',Employee1.age) #22