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
class CSE_fresher(CSE_student):

    def show_course(self):
        print("Available Courses are: CSE110, ENG101, MAT101, MAT110",
              "\nTo add any course Type: Add_CSE110")

    def Add_CSE110(self):
        print("Course CSE110 Added.")

    def Add_ENG101(self):
        print("Course ENG101 Added.")

    def Add_MAT101(self):
        print("Course MAT101 Added.")

    def Add_MAT110(self):
        print("Course MAT110 Added.")
#========================================================
s1 = CSE_fresher("Mohammad Shariful Alam Mollah",20201146,3)
s1.cse_details()
print("=====================================")
s1.show_course()
print('===================================')
s1.Add_ENG101()
