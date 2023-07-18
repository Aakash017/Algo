class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.tail.next = node
        self.head.prev = node

    def insert(self, value, location):
        node = Node(value)
        if location == 0:
            node.next = self.head.next
            node.prev = self.head.prev
            self.head = node
            self.tail.next = node
        elif location == -1:
            node.next = self.tail.next
            node.prev = self.tail.prev
            self.tail.next = node
            self.tail = node
            self.head.prev = node
        else:
            tmp = self.head
            for _ in range(location - 1):
                tmp = tmp.next
            tmp.next.prev = node
            node.next = tmp.next
            tmp.next = node
            node.prev = tmp

    def traverse(self):
        tmp = self.head
        while tmp:
            print(tmp.prev.value, "<------", tmp.value, "-------->", tmp.next.value)
            if tmp.next == self.head:
                break
            tmp = tmp.next

    def reverse_traverse(self):
        tmp = self.tail
        while tmp:
            print(tmp.prev.value, "<------", tmp.value, "-------->", tmp.next.value)
            if tmp.prev == self.tail:
                break
            tmp = tmp.prev

    def search(self, value):
        tmp = self.head
        while tmp:
            if tmp.value == value:
                return tmp.value
            if tmp.next == self.head:
                break
            tmp = tmp.next
        return "not found"

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        if index == -1:
            self.tail.prev.next = self.tail.next
            self.tail = self.tail.prev
            self.head.prev = self.tail
        else:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
            prev = tmp.prev
            next = tmp.next
            curr = tmp
            prev.next = curr.next
            next.prev = curr.prev

    def delete_all(self):
        tmp = self.head
        while tmp:
            tmp.prev = None
            if tmp.next==self.head:
                break
            tmp = tmp.next

        self.head = None
        self.tail = None

    def __iter__(self):
        tmp = self.head
        while tmp:
            yield tmp
            if tmp.next == self.head:
                break
            tmp = tmp.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


cdll = CircularDoubleLinkedList()
cdll.createCDLL(1)

cdll.insert(2, 0)
cdll.insert(3, -1)
cdll.insert(4, 1)
cdll.insert(5, 2)
cdll.traverse()
# print(cdll.search(6))
print("\n")
# cdll.reverse_traverse()
print([node.value for node in cdll])
cdll.delete(2)
print([node.value for node in cdll])
cdll.traverse()

# cdll.delete_all()
# print([node.value for node in cdll])

