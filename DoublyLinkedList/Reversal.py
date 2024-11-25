from BasicMethods import Node, DoubLinkedList

def Reverse(mylist):
    temp = None
    curr = mylist.head
    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    if temp:
        mylist.head = temp.prev
    mylist.Print()

obj = DoubLinkedList()
obj.Append(123)
obj.Append(456)
obj.Prepend(789)
obj.Append(104)
obj.Prepend(103)
obj.Print()
print(" ")
Reverse(obj)