from collections import deque

#s = "Hello"
#print(list(s))

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
    

def reverse_string(s):                                 
    stack = Stack()

    for ch in s:                             # for characters in s push the characters into the rev_string blank thing
        stack.push(ch)

    rev_str = ''
    while stack.size()!=0:
        rev_str += stack.pop()

    return rev_str

if __name__ == '__main__':
    print(reverse_string("Hello I am Srijit"))

