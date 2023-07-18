class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            # if node.next == self.head:
            #     break
            node = node.next

    # creation of double linked list
    def createDLL(self, nodevalue):
        node = Node(nodevalue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    def insert(self, nodevalue, location):
        node = Node(nodevalue)
        if location == 0:
            node.next = self.head
            # node.prev = None
            self.head.prev = node
            self.head = node
        elif location == -1:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            tmp = self.head
            for _ in range(location):
                tmp = tmp.next
            node.prev = tmp
            node.next = tmp.next
            tmp.next.prev = node
            tmp.next = node

    def delete(self, location):
        if location == 0:
            self.head = self.head.next
            self.head.prev = None
        elif location == -1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            tmp = self.head
            for _ in range(location):
                tmp = tmp.next
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp.next = None
            tmp.prev = None

    def search(self, value):
        tmp = self.head
        while tmp:
            if tmp.value == value:
                return tmp
            tmp = tmp.next
        return "Not found"

    def traverse(self):
        tmp = self.head
        while tmp:
            print(tmp.prev.value if tmp.prev else "", "<----", tmp.value, "---->", tmp.next.value if tmp.next else "")
            tmp = tmp.next

    def reverse_traverse(self):
        tmp = self.tail
        while tmp:
            print(tmp.value)
            tmp = tmp.prev

    def delete_all(self):
        tmp = self.head
        while tmp:
            tmp.prev = None
            tmp = tmp.next
        self.head = None
        self.tail = None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


doublell = DoubleLinkedList()
doublell.createDLL(1)
doublell.insert(2, 0)
doublell.insert(3, 0)
doublell.insert(4, 0)
doublell.insert(5, -1)
print([node.value for node in doublell])

# doublell.insert(6, 2)

# print(doublell.search(3))
# doublell.search(3)
# doublell.delete(0)
# doublell.delete(-1)
# doublell.delete(2)
doublell.delete_all()
print([node.value for node in doublell])

doublell.traverse()
doublell.reverse_traverse()
