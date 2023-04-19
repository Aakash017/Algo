class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n5 = Node(50)
n4.next = n5


class LinkedList:
    def __init__(self, head):
        self.head = head

    def traverse(self):
        if self.head is None:
            print("LinkedList Is empty")
        else:
            tmp = self.head
            while tmp:
                print(tmp.data)
                tmp = tmp.next

    def add_node_in_last(self, Node):
        if self.head is None:
            print("LinkedList Is empty")
            self.head = Node
        else:
            tmp = self.head
            while tmp.next:
                # print(tmp.data, "->")
                tmp = tmp.next
            tmp.next = Node

    def add_node_in_starting(self, Node):
        if self.head is None:
            print("LinkedList Is empty")
            self.head = Node
        else:
            tmp = self.head
            self.head = Node
            self.head.next = tmp

    def add_node_after_k(self, Node, k):
        temp = self.head
        while temp:
            if k == temp.data:
                t = temp.next
                temp.next = Node
                Node.next = t
                temp = temp.next
            else:
                temp = temp.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next, 20, 30
            current.next = prev, None, 10
            prev = current, 10, 20
            current = next, 20, 30
        self.head = prev

    def reverse_2(self):
        if self.head is None:
            print("LinkedList is empty so it cannot be reversed")
        else:
            tmp = self.head
            prev = None
            while tmp.next:
                print("comers here")
                _prev = tmp.next
                tmp.next = prev
                prev = _prev


l = LinkedList(n1)
# l.traverse()
n6 = Node(60)
n7 = Node(70)
l.add_node_in_last(n6)
# l.traverse()
l.add_node_in_starting(n7)
# l.traverse()

n8 = Node(80)
l.add_node_after_k(n8, 30)
l.traverse()
l.reverse_2()
print("reverse compte")
l.traverse()

# 10->20->30->40->50
#
# 50->40->30->20->10
