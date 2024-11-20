from LinkedList.BasicFucntions import node, LinkedList

def GetNthFromLast(l1, n):
    curr_node = l1.head
    TotalLength = l1.LenRecur(l1.head)
    while curr_node:
        if TotalLength==n:
            print("The " + str(n) + "th element from the last is " + str(curr_node.data))
        curr_node = curr_node.next
        TotalLength -= 1

obj = LinkedList()
obj.Append(123)
obj.Append(456)
obj.Prepend(789)
obj.InsertAtPos(obj.head.next.next, 101)
obj.Print()
GetNthFromLast(obj, 4)