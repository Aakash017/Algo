"""
Implement queue using stack
"""


class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()


class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueu(self, item):
        self.inStack.push(item)

    def deque(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

customequeue=Queue()
customequeue.enqueu(1)
customequeue.enqueu(2)
customequeue.enqueu(3)
print(customequeue.deque())
