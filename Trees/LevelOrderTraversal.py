from QueueModule import Queue

class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinTree:
    def __init__(self, root):
        self.root = Node(root) 

    def LevelOrder(self, start):
        if start is None:
            return 
        traverse = ""
        q = Queue()
        q.enq(start)
        while len(q) > 0:
            traverse += str(q.peek()) + "-"
            node = q.deq()
            if node.left:
                q.enq(node.left)
            if node.right:
                q.enq(node.right)
        return traverse

tree = BinTree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(6)
tree.root.right = Node(7)
tree.root.right.right = Node(8)
tree.root.right.right.left = Node(9)
print(tree.LevelOrder(tree.root))