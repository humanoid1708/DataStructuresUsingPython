class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CirLinkedList:
    def __init__(self):
        self.head = None

    def Len(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count
        
        
    def Print(self):
        if not self.head:
            print("List does not exists")
        else:
            curr_node = self.head
            while True: 
                print(curr_node.data)
                curr_node = curr_node.next
                if curr_node == self.head:
                    break

    def Append(self, data):
        if not self.head:
            self.head = node(data)
            self.head.next = self.head
        else:
            new_node = node(data)
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head
        
    def Remove(self, key):
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr.data == key:
                    prev.next = curr.next
                    curr = curr.next
'''
obj = CirLinkedList()
obj.Append(123)  
obj.Append(456)  
obj.Append(789)  
print(obj.Len())
obj.Print()
obj.Remove(789)
obj.Print()
'''
                

                

             

    