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
            
obj = BST(10)
obj.Insert(3)
obj.Insert(4)
obj.Insert(7)
obj.Insert(12)
obj.Insert(17)
obj.Insert(15)
obj.Insert(2)

print(obj.Search(12))
print(obj.Search(5))
print(obj.Search(15))


