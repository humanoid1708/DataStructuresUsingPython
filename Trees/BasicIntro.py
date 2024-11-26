class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinTree:
    def __init__(self, root):
        self.root = Node(root) 

'''   
tree = BinTree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(6)
tree.root.right = Node(7)
tree.root.right.right = Node(8)
tree.root.right.right.left = Node(9)
'''