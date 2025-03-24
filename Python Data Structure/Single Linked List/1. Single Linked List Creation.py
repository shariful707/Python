class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Single_Linked_List:
    def __init__(self,data):
        new_node= Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
# class Single_Linked_List:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0


node1 = Node(10)
print(node1.data)
print(node1)

list = Single_Linked_List(20)
print(list.head)
print(list.tail.data)