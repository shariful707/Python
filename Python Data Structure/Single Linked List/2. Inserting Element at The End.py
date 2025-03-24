from traceback import print_list


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data): #Appending at last
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = self.length+1

        else:
            self.tail.next = new_node #self.tail = 10/20 then self.tail.next = 10/20.next = None turn to new nodes reference
            self.tail = new_node
            self.length += 1

    def __str__(self): #here printing by default using print(obj)
        temp = self.head
        result = ''
        while temp != None:
            result += str(temp.data)

            if temp.next != None:
                result += "->"
            temp = temp.next
        return result

    def printlist(self): #Here printing the values in array
        arr1 = []
        temp = self.head
        while temp != None:
            arr1.append(temp.data)
            temp = temp.next
        return arr1

list1 = Single_Linked_List()
list1.append(10)
list1.append(20)
list1.append(30)
print(list1)
print(list1.head)
print(list1.length)
print(list1.tail)
print(list1.printlist())


