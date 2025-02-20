class student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id #Here the instance variable is privatized which can not be accessed outside of the class

    def info(self):
        print("Student's Name is",self.name,
              "\n& The ID is:",self.__id)
        self.__private_method() # Here the the private method is executed and called which is its characteristics

    def update_id(self,id):
        if id>0:
            self.__id = id
        else:
            print("This is an error ID. Please try again with valid ID")
    def get_id(self):
        return self.__id

    def __private_method(self): #Here private method is created inside of the class
        print("Private Method is Executed!")
s1 = student("Mohammad Shariful Alam Mollah",20201146)
s1.info()
print("=======================")
s1.__id = -60
print("It created another instance to store that value not the main on is manilpulated")
print(s1.__id)
print("Here is it",
      "\n",s1.__dict__,'__id is the new created one')
s1.update_id(24201146)
print("===========================")
s1.info()
print("============================")
print(s1.get_id())