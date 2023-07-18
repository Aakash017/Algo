class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node

    def inser_node_at_start(self, nodevalue):
        node = Node(nodevalue)
        node.next = self.head
        self.head = node
        self.tail.next = node

    def insert_node_at_last(self, nodevalue):
        new_node = Node(nodevalue)
        # self.tail.next = node
        # node.next = self.head
        self.tail.next=new_node
        self.tail=new_node
        self.tail.next=self.head

    def insert_node_at_location(self, nodevalue, index):
        node = Node(nodevalue)
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        node.next = tmp.next
        tmp.next = node

    def traversalCSLL(self):
        if self.head is None:
            print("No Node")
        else:
            tmp = self.head
            while tmp:
                print(tmp.value)
                tmp = tmp.next
                if tmp == self.head:
                    break

    def search(self, value):
        tmp = self.head
        while tmp:
            if tmp.value == value:
                return tmp
            tmp = tmp.next
            if tmp == self.head:
                break
        return f"{value} not found in List"

    def delete_node(self, index):
        if index == 0:
            self.head=self.head.next
            self.tail.next=self.head
        elif index == -1:
            tmp = self.head
            while tmp.next.next != self.head:
                tmp = tmp.next
            tmp.next = self.head
            self.tail = tmp
        else:
            tmp = self.head
            c = 0
            while c < index - 1:
                tmp = tmp.next
                if tmp.next==self.head:
                    break
            tmp.next = tmp.next.next
    def deleteCSLL(self):
        self.head=None
        # self.tail.next=None
        self.tail=None


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# l1 = Node(1)
# l2 = Node(2)
# l1.next = l2
# l3 = Node(3)
# l2.next = l3
# l4 = Node(4)
# l3.next = l4
# l5 = Node(5)
# l4.next = l5
# l6 = Node(6)
# l5.next = l6
# l7 = Node(7)
# l6.next = l7

c = CircularLinkedList()
c.createCSLL(1)
c.inser_node_at_start(4)
c.inser_node_at_start(3)
c.inser_node_at_start(2)
c.insert_node_at_last(5)
c.insert_node_at_last(6)
c.insert_node_at_last(7)
c.insert_node_at_last(8)
c.insert_node_at_last(9)
c.insert_node_at_last(10)
c.insert_node_at_last(11)
# c.insert_node_at_location(3, 1)
c.traversalCSLL()
print("\n")
# c.delete_node(0)
c.delete_node(1)
c.deleteCSLL()
c.traversalCSLL()

# print(c.search(6))

# print([node.value for node in c])
