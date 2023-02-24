from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


    def front(self):
        return self.buffer[-1]
    

def produce_binary_numbers(n):
    binary_numbers = Queue()
    binary_numbers.enqueue("1")

    for i in range(n):
        front = binary_numbers.front()
        print("  ",front)

        binary_numbers.enqueue(front + "0")
        binary_numbers.enqueue(front + "1")

        binary_numbers.dequeue()

if __name__ == '__main__':
    produce_binary_numbers(10)        


