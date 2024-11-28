class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinTree:
    def __init__(self, root):
        self.root = Node(root)

    def Height(self, start):
        if start is None:
            return - 1
        left_height = self.Height(start.left)
        right_height = self.Height(start.right)

        return 1+max(left_height, right_height)
    
    def Size(self, start):
        if start is None:
            return 0

        return 1 + self.Size(start.left) + self.Size(start.right)
    
    def size(self):
        if self.root is None:
            return 0

        stack = []
        stack.append(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1 
                stack.append(node.right)
        return size

        


tree = BinTree("F")
tree.root.left = Node("B")
tree.root.left.left = Node("A")
tree.root.left.right = Node("D")
tree.root.left.right.left = Node("C")
tree.root.left.right.right = Node("E")
tree.root.right = Node("G")
tree.root.right.right = Node("I")
tree.root.right.right.left = Node("H") 
print(tree.size())
