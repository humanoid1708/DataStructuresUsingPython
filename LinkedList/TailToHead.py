from BasicFucntions import node, LinkedList

def MoveTailToHead(mylist):
    curr = mylist.head
    prev = None

    while curr.next:
        prev = curr
        curr = curr.next
    prev.next = None
    curr.next = mylist.head
    mylist.head = curr

l1 = LinkedList()
l1.Append("a")
l1.Append("b")
l1.Append("c")
l1.Append("d")
l1.Append("e")
l1.Append("f")
l1.Append("g")
l1.Print()
MoveTailToHead(l1)
l1.Print()