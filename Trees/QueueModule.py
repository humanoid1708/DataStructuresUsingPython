class Queue(object):
    def __init__(self):
        self.items = []

    def enq(self, data):
        self.items.insert(0, data)

    def deq(self):
        if not self.isempty():
            return self.items.pop()
    
    def isempty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.isempty():
            return self.items[-1].data
    def __len__(self):
        return self.size()
    
    def size(self): 
        return len(self.items)