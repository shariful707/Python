class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

class CQueue:
    def __init__(self):
        self.list = LinkedList()

    def isEmpty(self):
        if self.list.head == None:
            return True
        else:
            return False

    def enqueue(self,val):
        new_node = Node(val)
        if self.isEmpty() == True:
            self.list.head = new_node
            self.list.tail = new_node
            self.list.size += 1
        else:
            x = self.list.tail
            x.next = new_node
            self.list.tail = new_node
            self.list.size += 1

    def printQueue(self):
        if self.isEmpty() == True:
            print("Queue is Empty")
        else:
            curr = self.list.head
            for i in range(0,self.list.size):
                print(curr.value)
                curr = curr.next

    def dequeue(self):
        if self.isEmpty() == True:
            print("Nothing to enqueue, it is empty")
        else:
            x = self.list.head
            print(x.value)
            y = x.next
            self.list.head = y
            self.list.size -=1

    def peek(self):
        if self.isEmpty() == True:
            print('The Queue is empty')
        else:
            print(self.list.head.value)

    def delete(self):
        self.list.head = None
        self.list.tail = None
        self.list.size = 0

queue = CQueue()
print(queue.isEmpty())
queue.printQueue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.printQueue()
queue.dequeue()
print('after dequeue')
queue.printQueue()
