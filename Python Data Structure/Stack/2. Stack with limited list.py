class CustomStack:
    def __init__(self,maxSize):
        self.list = []
        self.size = maxSize

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)==self.size:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull()== True:
            return "No place to Insert"
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty() == True:
            return "Nothing to pop"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty()==True:
            return "Nothing to peek"
        else:
            return self.list[len(self.list)-1]

    def printStack(self):
        for i in range(len(self.list)-1,-1,-1):
            print(self.list[i])

stack = CustomStack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.printStack()
print(stack.peek())
print(stack.isEmpty())
print(stack.isFull())
print("New")
print(stack.pop())
print("after pop")
stack.printStack()

