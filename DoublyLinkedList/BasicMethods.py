class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubLinkedList:
    def __init__(self):
        self.head = None
    
    def Print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        
    def Append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = None
            self.head.prev = None

        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.next = None
            new_node.prev = curr


    def Prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = None
            self.head.prev = None

        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
    
    def AddBefore(self, key, data):
        if key == self.head.data:
            self.Prepend(data)
        else:
            curr = self.head
            pre = None
            new = Node(data)
            while curr.data != key:
                pre = curr
                curr = curr.next
            curr.prev = new
            new.next = curr
            pre.next = new
            new.prev = pre

    #mistake
    def AddAfter(self, key, data):
        curr = self.head
        pre = None
        new = Node(data)
        while curr.next != None:
            pre = curr
            curr = curr.next
        curr.prev = new
        new.next = curr
        pre.next = new
        new.prev = pre

    def DeleteNode(self, key):
        curr = self.head
        pre = None
        if self.head.data ==  key:
            temp = curr.next
            curr.next = None
            temp.prev = None
            self.head = temp
        while curr.next != None:
            pre = curr
            curr = curr.next
            if curr.data == key:
                if curr.next == None:
                    pre.next = None
                else:
                    pre.next = curr.next
                    curr.next.prev = pre
                    curr.prev = None
                    curr.next = None
                    
'''
obj = DoubLinkedList()
obj.Append(123)
obj.Append(456)
obj.Prepend(789)
obj.Print()
print(" ")
obj.DeleteNode(123)
obj.Append(104)
obj.Prepend(103)
obj.Print()
'''            

        
