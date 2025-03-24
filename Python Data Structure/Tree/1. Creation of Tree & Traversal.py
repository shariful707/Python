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

def InOrder(tree):
    if tree is None:
        return
    InOrder(tree.left)
    print(tree.data)
    InOrder(tree.right)

def PostOrder(tree):
    if tree is None:
        return
    PostOrder(tree.left)
    PostOrder(tree.right)
    print(tree.data)

def height(tree):
    if tree is None:
        return 0
    left_height = height(tree.left)
    right_height = height(tree.right)
    return 1 + max(left_height, right_height)

# Function to print nodes at a given level
def printLevel(tree, level):
    if tree is None:
        return
    if level == 1:
        print(tree.data)  # Print node data
    elif level > 1:
        printLevel(tree.left, level - 1)
        printLevel(tree.right, level - 1)

# Level Order Traversal using recursion
def LevelOrder(tree):
    h = height(tree)  # Get the height of the tree
    for i in range(1, h + 1):
        printLevel(tree, i)


root = TreeNode('Drinks')
c2 = TreeNode('Hot')
c3 = TreeNode('Cold')
c4 = TreeNode('Tea')
c5 = TreeNode('Coffee')
c6 = TreeNode('Cola')
c7 = TreeNode('Fanta')

root.left = c2
root.right = c3
c2.left = c4
c2.right = c5
c3.left = c6
c3.right = c7
print("preorder Traversal:")
PreOrder(root)
print("Inorder Traversal:")
InOrder(root)
print('Post Order:')
PostOrder(root)
print('Level Order:')
LevelOrder(root)