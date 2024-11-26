class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinTree:
    def __init__(self, root):
        self.root = Node(root) 

    def pre_order(self, start, traverse):
        if start:
            traverse += (str(start.data) + "-")
            traverse =  self.pre_order(start.left, traverse)
            traverse =  self.pre_order(start.right, traverse)
        return traverse
    def in_order(self, start, traverse):
        if start:
            traverse = self.in_order(start.left, traverse)
            traverse += (str(start.data) + "-")
            traverse = self.in_order(start.right, traverse)
        return traverse
    def post_order(self, start, traverse):
        if start:
            traverse = self.post_order(start.left, traverse)
            traverse = self.post_order(start.right, traverse)
            traverse += (str(start.data) + "-")
        return traverse

    
tree = BinTree("F")
tree.root.left = Node("B")
tree.root.left.left = Node("A")
tree.root.left.right = Node("D")
tree.root.left.right.left = Node("C")
tree.root.left.right.right = Node("E")
tree.root.right = Node("G")
tree.root.right.right = Node("I")
tree.root.right.right.left = Node("H")
print(tree.pre_order(tree.root, " "))
print(tree.in_order(tree.root, " "))
print(tree.post_order(tree.root, " "))
