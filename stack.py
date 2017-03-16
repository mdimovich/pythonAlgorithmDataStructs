# Stack implemented in python


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# Reverse a string using a stack
def reverseStr(m):
    s = Stack()
    strRev = ""
    for index in range(0, len(m)):
        s.push(m[index])
    for index in range(0, s.size()):
        strRev += s.pop()
    return strRev

# Balanced parentheses: Determines if a parentheses entered in an equation are balanced
def parBalance(parStr):
    stack = Stack()
    for index in range(0, len(parStr)):
        if parStr[index] == '(':
            stack.push(parStr[index])
        elif parStr[index] == ')':
            if stack.isEmpty():
                return False
            else:
                stack.pop()

    if stack.isEmpty():
        return True
    else:
        return False



stack = Stack()
reverse = ""
name = "michael"
print(stack.isEmpty())
stack.push("michael")
print(stack.isEmpty())
stack.push("cookie")
print(stack.peek())
stack.push("Dog")
print(stack.size())
stack.pop()
print(stack.size())
print("Reversing a string using a stack: ")
reverse = reverseStr(name)
print("The reversed string: ", reverse)

print(parBalance("(()()()())"))
