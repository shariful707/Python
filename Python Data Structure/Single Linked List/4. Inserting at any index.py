class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
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
            self.tail.next = new_node #self.tail = 10/20 then self.tail.next = 10/20.next = None turn to new nodes reference
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

    def printlist(self): #Here printing the values in array
        arr1 = []
        temp = self.head
        while temp != None:
            arr1.append(temp.data)
            temp = temp.next
        return arr1

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

list1 = SingleLinkedList()
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
print(list1.length)
list1.insert(7,21)
print(list1.printlist())
print(list1.length)
list1.insert(-2,31)