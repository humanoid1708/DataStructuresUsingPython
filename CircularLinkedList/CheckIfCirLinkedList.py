from BasicOperations import node, CirLinkedList

def Check(Mylist):
    curr = Mylist.head
    while curr.next:
        curr= curr.next
        if curr.next == Mylist.head:
            return True
        
    return False

l1 = CirLinkedList()
l1.Append("A")
l1.Append("B")
print(Check(l1))