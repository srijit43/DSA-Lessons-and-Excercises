#is_balanced("({a+b})")     --> True
#is_balanced("))((a+b}{")   --> False
#is_balanced("((a+b))")     --> True
#is_balanced("))")          --> False
#is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True



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
    

def is_match(ch1,ch2):
    match_dict = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    return match_dict[ch1]==ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch==']':
            if stack.size==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
            
    return stack.size()==0

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    


     

