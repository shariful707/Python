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

def search(tree,val):
    if tree is None:
        #print("Match Not Found")
        return 'Match not Found'
    if tree.data == val:
        print("Match Found")
        return "Match found"
    else:
        search(tree.left,val)
        search(tree.right, val)
        return


# def search(tree, val):
#     if tree is None:
#         return False  # Match not found
#
#     if tree.data == val:
#         print("Match Found")
#         return True  # Stop searching further
#
#     # Search left and right subtrees
#     found_in_left = search(tree.left, val)
#     if found_in_left:  # If found in left subtree, stop searching
#         return True
#
#     found_in_right = search(tree.right, val)
#     return found_in_right  # Return True if found, otherwise False


root = TreeNode('Drinks')
c2 = TreeNode('Hot')
c3 = TreeNode('Cold')
c4 = TreeNode('Tea')
c5 = TreeNode('Coffee')

root.left = c2
root.right = c3
c2.left = c4
c2.right = c5

search(root,'Tea')