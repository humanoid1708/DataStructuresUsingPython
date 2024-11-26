from QueueModule import Queue
from BasicIntro import Node, BinTree

def RevLevelOrder(start):
    if start is None:
        return
    q = Queue()
    s = []
    q.enq(start)
    while len(q) > 0:
        node = q.deq()
        s.append(node.data)
        if node.right:
            q.enq(node.right)
        if node.left:
            q.enq(node.left)
    traverse = ""
    while len(s) > 0:
        traverse += (str(s.pop()) + "-")
    return traverse

tree = BinTree(1)  
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(RevLevelOrder(tree.root))

    

