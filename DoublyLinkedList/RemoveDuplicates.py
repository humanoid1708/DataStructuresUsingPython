from BasicMethods import Node, DoubLinkedList

def RemoveDup(mylist):
    curr = mylist.head
    count = {}
    while curr:
        count[curr.data] = 1
        curr = curr.next
    
    print(count)

dll = DoubLinkedList()
dll.Append(101)
dll.Append(102)
dll.Append(103)
dll.Append(102)
dll.Append(102)
dll.Append(104)
dll.Print()
print(" ")

RemoveDup(dll)

