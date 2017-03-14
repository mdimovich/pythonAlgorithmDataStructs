# Stack implemented in python using lists


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

stack = Stack()

print(stack.isEmpty())
stack.push("michael")
print(stack.isEmpty())
stack.push("cookie")
print(stack.peek())
stack.push("Dog")
print(stack.size())
stack.pop()
print(stack.size())
