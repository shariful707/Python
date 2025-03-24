class BSTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(tree,val):
    if tree.data is None:
        tree.data = val
        return
    elif val < tree.data:
        if tree.left is None:
            tree.left = BSTree(val)
        else:
            insert(tree.left,val)
    else:
        if tree.right is None:
            tree.right = BSTree(val)
        else:
            insert(tree.right,val)
def InOrder(tree): #Actually sorting in ascending order
    if tree is None:
        return
    InOrder(tree.left)
    print(tree.data)
    InOrder(tree.right)

root = BSTree(None)
insert(root,95)
insert(root,70)
insert(root,105)
insert(root,65)
insert(root,35)
insert(root,100)
insert(root,120)
insert(root,10)
# print(root.data)
# print(root.left.data)
# print(root.right.data)
InOrder(root)