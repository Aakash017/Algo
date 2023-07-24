"""
Design a stack in which addition to push and pop there is min method which will return minimum element
push pop and min should be in O(1)
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.minnode = None

    def min(self):
        if not self.minnode:
            return None
        return self.minnode.value

    def push(self, item):
        if self.minnode and (self.minnode.value < item):
            self.minnode = Node(value=self.minnode.value, next=self.minnode)
        else:
            self.minnode = Node(value=item, next=self.minnode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.minnode:
            return None
        self.minnode = self.minnode.next
        item = self.top.value
        self.top = self.top.next
        return item


custom = Stack()
custom.push(5)
print(custom.min())
custom.push(6)
print(custom.min())
custom.push(3)
print(custom.min())
custom.pop()
print(custom.min())
