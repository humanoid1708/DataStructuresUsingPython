from BasicOperations import node, CirLinkedList

def SplitInTwo(mylist):
    leng = mylist.Len()
    if leng == 0:
        return None
    
    elif leng == 1:
        return mylist.head
    
    else:
        middle = leng//2
        curr1 = mylist.head
        count = 1
        while count != middle:
            curr1 = curr1.next
            count +=1

        list2 = CirLinkedList()
        list2.head = curr1.next
        curr1.next = mylist.head
        curr2 = list2.head
        while curr2.next != mylist.head:
            curr2 = curr2.next
        curr2.next = list2.head
    return mylist, list2
    

list1 = CirLinkedList()
list1.Append(2)
list1.Append(4)
list1.Append(6)
list1.Append(8)
list1.Append(1)
list1.Append(3)
list1.Append(5)
list1.Append(7)
list1, list2 = SplitInTwo(list1)
list1.Print()
print("     ")
list2.Print()