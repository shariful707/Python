class Tree:
    def __init__(self,size):
        self.size = size
        self.list = [None]* self.size
        self.lastInd= 0
        self.start = 1

    def insert(self,val):
        if self.lastInd +1 == self.size:
            print('The Tree is Full')
        else:
            self.list[self.lastInd+1] = val
            self.lastInd +=1

    def search(self,val):
        for i in range(1,self.lastInd+1):
            if self.list[i] == val:
                print("Match Found")
        return "Not Found"

    def printTree(self): #Level Order Traversal
        for i in range(1,self.lastInd+1):
            print(self.list[i])

    def PreOrder(self,ind):
        if self.lastInd == 0:
            print('Empty Tree')
            return
        elif ind > self.lastInd:
            return
        print(self.list[ind])
        self.PreOrder(2*ind)
        self.PreOrder(2*ind+1)

    def InOrder(self,ind):
        if self.lastInd == 0:
            print('Empty Tree')
            return
        elif ind > self.lastInd:
            return
        self.InOrder(2 * ind)
        print(self.list[ind])
        self.InOrder(2*ind+1)

    def PostOrder(self,ind):
        if self.lastInd == 0:
            print('Empty Tree')
            return
        elif ind > self.lastInd:
            return
        self.PostOrder(2 * ind)
        self.PostOrder(2*ind+1)
        print(self.list[ind])



l1 = Tree(10)
l1.insert('Drinks')
l1.insert("Hot")
l1.insert('Cold')
l1.insert('Tea')
l1.insert('Coffee')
l1.insert('Cola')
l1.insert('Fanta')
# l1.printTree()
l1.PreOrder(1)