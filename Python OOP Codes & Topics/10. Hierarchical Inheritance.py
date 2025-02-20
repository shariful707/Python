#It means 1 parents but more than 1 child can access the same parent
class Student:

    def __init__(self,name,ID):
        self.name = name
        self.id = ID

#+++++++++++++++++++++++++++++++++++++++++++++++++++
class CSE_student(Student):

    def __init__(self,name,ID,labs):
        super().__init__(name,ID)
        self.lab = labs

    def cse_details(self):
        print("Student Name:",self.name,
              "\nID:",self.id,
              "\nNumber of Lab:",self.lab)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
class BBA_student(Student):

    def __init__(self,name,id,presentation):
        super().__init__(name,id)
        self.pres = presentation

    def bba_details(self):
        print("Student Name:",self.name,
              "\nID:",self.id,
              "\nNumber of Presentation:",self.pres)
#========================================================
s1 = CSE_student("Anim",20201146,3)
s1.cse_details()
print('===================================')
s2 = BBA_student('Arnab',20201156,7)
s2.bba_details()