from BasicMethods import Node, DoubLinkedList

def Pair(mylist, sum):
    pair = list()
    p1 = mylist.head
    p2 = None
    while p1:
        p2 = p1. next
        while p2:
            if (p1.data + p2.data) == sum:
                pair.append("("+ str(p1.data) + "," + str(p2.data) + ")")
            p2 = p2.next
        p1 = p1.next
    print(pair)

obj = DoubLinkedList()
obj.Append(1)
obj.Append(2)
obj.Append(3)
obj.Append(4)
obj.Append(5)
obj.Append(6)
obj.Append(7)
obj.Append(8)
obj.Append(9)
obj.Append(10)
Pair(obj, 10)
