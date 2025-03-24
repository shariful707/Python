class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

class CStack:
    def __init__(self):
        self.list = LinkedList()

    def isEmpty(self):
        if self.list.head == None:
            return True
        else:
            return False

    def push(self,val):
        new_node = Node(val)
        if self.isEmpty() == True:
            self.list.head = new_node
            self.list.tail = new_node
            self.list.size += 1
        else:
            x = self.list.head
            new_node.next = x
            self.list.head = new_node
            self.list.size += 1

    def printStack(self):
        if self.isEmpty() == True:
            print("Stack is Empty")
        else:
            curr = self.list.head
            for i in range(0,self.list.size):
                print(curr.value)
                curr = curr.next

    def pop(self):
        if self.isEmpty() == True:
            print("Nothing to pop, it is empty")
        else:
            x = self.list.head
            print(x.value)
            y = x.next
            self.list.head = y
            self.list.size -=1

    def peek(self):
        if self.isEmpty() == True:
            print('The stack is empty')
        else:
            print(self.list.head.value)

    def delete(self):
        self.list.head = None
        self.list.tail = None
        self.list.size = 0

stack = CStack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.printStack()
print('Now popping')
stack.pop()
print('after popping')
stack.printStack()
stack.push(5)
print("pushed 5")
stack.printStack()
stack.peek()
print('deleting')
stack.delete()
print(stack.isEmpty())
