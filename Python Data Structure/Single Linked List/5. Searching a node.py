class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data): #Appending at last
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            self.tail.next = new_node #self.tail = 10/20 which is before value then self.tail.next = 10/20.next = None turn to new nodes reference
            self.tail = new_node
            self.length += 1

    def prepend(self,data): #Appending value at first

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = self.length+1

        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self,index,data):
        new_node = Node(data)
        if index <0 or index>self.length :
            print("Invalid Index")
        elif index ==0:
            self.prepend(data)
        elif index == self.length :
            self.append(data)
        else:
            temp = self.head
            for i in range(0,index-1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node
            self.length +=1

    def printlist(self): #Here printing the values in array
        arr1 = []
        temp = self.head
        while temp != None:
            arr1.append(temp.data)
            temp = temp.next
        return arr1

    def search(self,target):
        self.tar = target
        temp = self.head
        i=0
        while temp != None:
            if temp.data == self.tar:
                #print("Match found in Index",i,
                      #'\n',temp.data,'Equal',self.tar)
                break
            else:
                i = i+1
            temp = temp.next
        return i
    def getVal(self,index):
        self.index = index
        temp = self.head
        for i in range(0,self.index):
            temp = temp.next

        #print('In Index',self.index,"The Value is",temp.data)
        return temp.data

    def setVal(self,index,val):
        self.val = val
        self.index = index
        temp = self.head
        for i in range(0,self.index):
            temp = temp.next

        temp.data = self.val

    def popup(self):
        temp = self.head
        if self.head == None:
            return None

        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
            return temp.data

        else:
            self.head = temp.next
            temp.next = None
            self.length -=1
            return temp.data

    def remove(self,value):
        self.val = value
        temp = self.head
        ind = self.search(self.val)
        if ind ==0:
            self.head = None
            self.tail = None
            self.length -=1
            return temp.data
        # print(ind)
        else:
            for i in range(0,ind-1):
                temp = temp.next

            x = temp.next
            temp.next=x.next
            x.next = None
            self.length -=1
        return x.data
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0

list1 = SLL()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
print(list1.printlist())
list1.insert(2,50)
print(list1.printlist())
list1.insert(0,7)
print(list1.printlist())
print("Length",list1.length,"Number of Indexes",list1.length-1)
list1.insert(7,21)
print(list1.printlist())
print("Length",list1.length,"Number of Indexes",list1.length-1) #length is not index length mean how many items are here
print("Here Using Search method to get Index value of given Data")
list1.search(4)
print("Here Using Get method to get value of given Index")
list1.getVal(7)
print("Here Using Set method to change value of given Index")
list1.setVal(7,39)
print(list1.printlist())
print("Now pop up which means first value will be deleted and head will moved to second one")
list1.popup()
print(list1.printlist())
print("Length",list1.length,"Number of Indexes",list1.length-1)
print("Deleting Value")
print(list1.remove(50))
print(list1.printlist())
list1.delete()
print(list1.printlist())

