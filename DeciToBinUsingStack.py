from Stack import Stack

def DeciToBin(input_decimal):
    s = Stack()
    org_decimal = input_decimal
    output_binary = ""

    while input_decimal != 0:
        r = input_decimal%2
        input_decimal = input_decimal//2
        s.push(r)
    
    while not s.isEmpty():
        output_binary += str(s.pop())

    print("The binary equivalent of " + str(org_decimal) + " is " + str(output_binary))

Input = 197
DeciToBin(Input)

