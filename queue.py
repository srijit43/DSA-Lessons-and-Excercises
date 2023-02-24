stock_price = []
stock_price.insert(0,131.7)
stock_price.insert(0,133.2)
stock_price.insert(0,134.5)
print(stock_price)

from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(7)
q.appendleft(2)

#print(q.pop())

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
x = Queue()

x.enqueue({
    'company':'Walmart',
    'timestamp':'11:00 AM',
    'price': 131
})

x.enqueue({
    'company': 'Walmart',
    'timestamp':'11:01 AM',
    'price': 132.3
})

x.enqueue({
    'company': 'Walmart',
    'timestamp':'11:00 AM',
    'price': 133.5
})

print(x.buffer)

print(x.size())




