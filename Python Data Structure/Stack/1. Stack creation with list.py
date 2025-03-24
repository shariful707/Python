class Stack:

    def __init__(self):
        self.list = []


    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "Element is Pushed"

    def pop(self):
        if self.list == []:
            return False
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return False
        else:
            x = len(self.list)-1
            val = self.list[x]
            return val

    def delete(self):
        self.list = []




