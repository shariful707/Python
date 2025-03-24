class CQueue:
    def __init__(self,size):
        self.item = [None] * size
        self.size = size
        self.start = -1
        self.rear = -1

    def isFull(self):
        if self.rear+1 == self.start:
            print("This Queue is Full")
            return True
        elif self.start == 0 and self.rear +1 == self.size:
            print("This Queue id Full")
            return True
        else:
            print("This is Empty")
            return False
    def isEmpty(self):
        if self.start == -1:
            print("This Queue is Empty")
            return True
        else:
            print("Queue uis Not Empty")
            return False



