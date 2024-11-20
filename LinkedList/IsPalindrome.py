#This code will tell us whether a given linked list is palindrome or not

from BasicFucntions import node, LinkedList

def StringCheck(mylist):
    string = ""
    p = mylist.head.next
    while p:
        string += p.data
        p = p.next
    print(string)
    print(string[::-1])
    return string == string[::-1] 

l1 = LinkedList()
l1.Append("r")
l1.Append("a")
l1.Append("c")
l1.Append("e")
l1.Append("c")
l1.Append("a")
l1.Append("r")

print(StringCheck(l1))
