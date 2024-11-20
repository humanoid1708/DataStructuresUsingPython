from LinkedList.BasicFucntions import node, LinkedList

def Merge(l1, l2):
    p = l1.head.next  # Skip the HEAD node for the first list
    q = l2.head.next  # Skip the HEAD node for the second list
    merged_list = LinkedList()

    # Create a dummy node to simplify the merging logic
    dummy = node("DUMMY")
    s = dummy

    # Traverse both lists and merge them
    while p and q:
        if p.data <= q.data:
            s.next = p
            p = p.next
        else:
            s.next = q
            q = q.next
        s = s.next  # Advance the merged list's tail

    # Append the remaining nodes of either list
    if p:
        s.next = p
    if q:
        s.next = q

    # Set the merged list's head
    merged_list.head.next = dummy.next
    merged_list.Print()

obj1 = LinkedList()
obj2 = LinkedList()
obj1.Append(1)
obj1.Append(3)
obj1.Append(5)
obj1.Append(7)
obj2.Append(2)
obj2.Append(4)
obj2.Append(6)
Merge(obj1, obj2)    
    
