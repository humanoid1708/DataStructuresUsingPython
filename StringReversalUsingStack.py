from Stack import Stack
    
def reverse(instr):
    s = Stack()
    revstr= ""

    for i in range(len(instr)):
        s.push(instr[i])

    for i in range(len(instr)):
        revstr += s.pop()

    return revstr

input = "egdelwonK"
print("The string is " + reverse(input))