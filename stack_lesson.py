from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        if len(self.container)==0:
            print("Stack is empty")
            return

        return self.container.pop()

    def is_empty(self):
        len(self.container)==0

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

s = Stack()         

s.push(3)
s.push(5)
s.push(7)

print(s.peek())

print(s.pop())

print(s.size())
