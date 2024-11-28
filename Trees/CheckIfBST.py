from BasicIntro import Node, BinTree

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self, data):
        self.root = Node(data)
    
    def InsertAt(self, current, new):
        if current.data < new:
            if current.right:
                self.InsertAt(current.right, new)
            else:
                current.right = Node(new)

        else:
            if current.left:
                self.InsertAt(current.left, new)
            else:
                current.left = Node(new)

    def Insert(self, data):
        self.InsertAt(self.root, data)

    def SearchThis(self, current, target):
        if current:
            if current.data == target:
                return True
            elif current.data < target:
                return self.SearchThis(current.right, target)
            else:
                return self.SearchThis(current.left, target)
            
    def Search(self, target):
        return self.SearchThis(self.root, target)

def is_bst_satisfied(tree):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        val = node.data
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(tree.root)
    
obj = BST(10)
obj.Insert(3)
obj.Insert(4)
obj.Insert(7)
obj.Insert(12)
obj.Insert(17)
obj.Insert(15)
obj.Insert(2)
print(is_bst_satisfied(obj))

tree = BinTree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(6)
tree.root.right = Node(7)
tree.root.right.right = Node(8)
tree.root.right.right.left = Node(9)
print(is_bst_satisfied(tree))