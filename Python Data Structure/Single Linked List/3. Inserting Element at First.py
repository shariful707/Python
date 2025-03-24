class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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

list1 = Single_Linked_List()
list1.prepend(30)
list1.prepend(20)
list1.prepend(10)
print(list1.printlist())
list2 = Single_Linked_List()
list2.prepend(10)
list2.prepend(20)
list2.prepend(30)
print(list2.printlist())