class node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node("HEAD")

    def Print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        
    def Append(self,data):
        new_node = node(data)
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def Prepend(self, data):
        new_node = node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def InsertAtPos(self, prev_node, data):
        if not prev_node: 
            print("Previous node is not in the list.")
            return
        new_node = node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def DeleteNodeByKey(self, key):
        curr_node = self.head
        if key == curr_node.data:
            self.head = curr_node.next
            curr_node = None
        else:
            prev_node = None
            while curr_node.data != key:
                prev_node = curr_node
                curr_node = curr_node.next
            prev_node.next = curr_node.next
            curr_node = None

    def DeleteNodeByPos(self, pos):
        curr_node = self.head
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
        else:
            prev_node = None
            count = 0
            while count < pos:
                prev_node = curr_node
                curr_node = curr_node.next
                count += 1
            prev_node.next = curr_node.next
            curr_node = None
    
    def Len(self):
        curr_node = self.head
        count = 1
        while curr_node.next != None:
            count +=1
            curr_node = curr_node.next
        print("The length of the list is " + str(count))

    def LenRecur(self, node):
        if node == None:
            return 0
        return 1 + self.LenRecur(node.next)

'''
obj = LinkedList()
obj.Append(123)
obj.Append(456)
obj.Prepend(789)
obj.InsertAtPos(obj.head.next.next, 101)
obj.Print()
obj.Len()
print("The length of the list is " + str(obj.LenRecur(obj.head)))
obj.DeleteNodeByKey(123)
obj.DeleteNodeByPos(3)
obj.Print()
'''        
