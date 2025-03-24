class Queue:
    def __init__(self):
        self.q = []

    def printQueue(self):
        for i in self.q:
            print(i)

    def isEmpty(self):
        if self.q == []:
            return True
        else:
            return False

    def EnQueue(self,value):
        self.q.append(value)
        print("Enqueue Completed")

    def Dequeue(self):
        if self.isEmpty() == True:
            print("This is an empty Queue")
        else:
            print(self.q.pop(0))

    def peek(self):
        if self.isEmpty() == True:
            print("Queue is Empty")
        else:
            print(self.q[0])

    def delete(self):
        self.q = []

queue = Queue()
queue.printQueue()
print(queue.isEmpty())
queue.EnQueue(1)
queue.EnQueue(2)
queue.EnQueue(3)
queue.EnQueue(4)
queue.EnQueue(5)
queue.printQueue()
queue.Dequeue()
print("after dequeue")
queue.printQueue()
queue.peek()
queue.delete()
print(queue.isEmpty())