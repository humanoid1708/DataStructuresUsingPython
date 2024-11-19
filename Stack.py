class Stack():
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()
    
    def isEmpty(self):
        return self.arr == []
    
    def peek(self):
        if not self.isEmpty():
            return self.arr[-1]
    
    def display(self):
        return self.arr
"""  
s = Stack()
print(s.isEmpty())
s.push("Apple")
s.push("Banana")
s.push("Cherry")
print(s.display())
print("The popped element is " + str(s.pop()))
print(s.display())
print("The topmost element is " + str(s.peek()))
s.pop()
print(s.display())
"""