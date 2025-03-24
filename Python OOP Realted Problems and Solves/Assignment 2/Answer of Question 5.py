class Student:
    def __init__(self,name = None):
        self.name = name
        if self.name == None:
            print("Hello Default Student")
        else:
            print("Hello",self.name)

    def quizcalc(self,*num):
        x = 0
        if len(num)==0:
            self.avg_score = 0
        else:
            for i in num:
                x = i + x

        self.avg_score = x/3


    def printdetail(self):
        print("Your Average Quiz Score:", self.avg_score)




s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()