from runpy import run_path


class Animal:
    def __init__(self,type,name,action):
        self.type = type
        self.name =  name
        self.action = action

    def info(self):
        print("This is",self.name,
              "\nThis is a",self.type,
              "\nThis",self.type,"is",self.action)

    def compare(self,ref): #Here ref taking the RAM's slot number of the different object to use all the variables value on another object
        if self.type == ref.type:
            if self.action == ref.action:
                print("Both",self.type,"are",self.action)
            else:
                print("Same type of animals are doing different action")
        else:
            if self.action == ref.action:
                print("Different animals are",self.action)
            else:
                print("Different animals are doing different action")

cat1 = Animal("cat","piku","Jumping")
cat2 = Animal("cat","pikumin","relaxing")
dog1 = Animal("dog","shawn","Jumping")
print("====================================================")
cat1.info()
print("=======================")
cat2.info()
print("===========================")
dog1.info()
print("===============================")
print("cat1 and cat2")
cat1.compare(cat2)
print('========================')
print("dog1 and cat1")
dog1.compare(cat1)