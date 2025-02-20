class Student:
    university = "BRACU" #This one can be accessible even though the object is not created

    def __init__(self,name,ID,dept):
        self.name = name
        self.id = ID
        self.dept = dept

    def details(self):
        print("Student Name:",self.name,
              "\nStudent ID:",self.id,
              "\nStudent Department:",self.dept,
              "\nUniversity:",Student.university)

    def update_uni(self,uni):
        self.university = uni
        print(self.university)

    @classmethod
    def change_uni_all(cls,uni):
        Student.university = uni

    @classmethod
    def split_up(cls,str):
        name,ID,dept = str.split('-')
        obj = cls(name, ID, dept) #here cls = Student class
        return obj #This return to the part it was called

    @staticmethod
    def dept_checker(ID): #This one can be accessible even though the object is not created
        ID = str(ID)
        if str(ID[3:5])=='01':
            print("Department of the Student is: CSE")
        elif str(ID[3:5])=='41':
            print("Department of the Student is: CS")

s1 = Student("Mohammad Shariful Alam Mollah",20201146,"CSE")
s2 = Student("Mehedi Hasan Rizvi",20201148,"CSE")
s3 = Student.split_up("Mujtaba Wasif-20201144-CSE") #Here it will return the object with class and will store s3 reference value
s4 = Student.split_up("Mourika Nigar-20241146-CS")
s1.details()
print("=================================")
s2.details()
print("=============================")
#now will change the name of uni in s2 object by instance method will change only for s2 not s1
s2.update_uni("BRAC University")
s2.details()
print('+++++++++++++++++++++++++++')
s1.details()
print('========================================')
#but now will change for every object
s1.change_uni_all("BRAC University")
s1.details()
s2.details()
s3.details()
print('===============================')
s4.details()
print('================')
Student.dept_checker(s4.id) # Here we call the Class the Student Class to access static or class method
print('====================')
Student.dept_checker(s1.id)