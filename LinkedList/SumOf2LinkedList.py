#Sum of 2 lists without carry
from BasicFucntions import node, LinkedList

def Node(data):
    NODE = node(data)
    return NODE

def PrintNum(mylist):
    num = ""
    curr = mylist.head.next
    while curr:
        num += str(curr.data)
        curr = curr.next
    print(num[::-1])

def sum(l1, l2):
    l3 = LinkedList()
    p = l1.head.next
    q = l2.head.next
    while p and q:
        l3.Append(p.data + q.data)
        p = p.next
        q = q.next
    while p:
        l3.Append(p.data)
        p = p.next
    while q:
        l3.Append(q.data)
        q = q.next

    PrintNum(l3)

l1 = LinkedList()
l2 = LinkedList()

l1.Append(2)
l1.Append(4)
l1.Append(5)
l1.Append(7)
l1.Append(9)
l2.Append(1)
l2.Append(4)
l2.Append(2)
PrintNum(l1)
PrintNum(l2)
sum(l1, l2)
    
