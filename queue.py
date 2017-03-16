# Queue implemented in Python

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)


