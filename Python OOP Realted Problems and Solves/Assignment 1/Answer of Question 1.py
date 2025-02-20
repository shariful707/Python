class DataType:
    def __init__(self,name,value):
        self.name = name #Here look into Question and check in print statement it derives from the class using object.name object.value
        self.value = value # That is why instance variable are name and value


data_type1 = DataType("Integer",1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType("String",'Hello')
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType('Float',4.0)
print(data_type3.name)
print(data_type3.value)