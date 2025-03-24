#need to imporve
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(tree):
    if tree is None:
        return
    print(tree.data)
    PreOrder(tree.left)
    PreOrder(tree.right)

def Insert(tree,val):
    if tree is None:
        root = TreeNode(val)
        return
    elif tree.left is None:
        tree.left = TreeNode(val)
    elif tree.right is None:
        tree.right = TreeNode(val)
    else:
        Insert(tree.left,val)


root = TreeNode('Drinks')
c2 = TreeNode('Hot')
c3 = TreeNode('Cold')
c4 = TreeNode('Tea')
c5 = TreeNode('Coffee')

root.left = c2
root.right = c3
c2.left = c4
c2.right = c5

Insert(root,'Cola')
Insert(root,'Fanta')
PreOrder(root)