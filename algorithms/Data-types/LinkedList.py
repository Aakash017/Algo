class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def print_linked_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def add_node_at_tail(self, data):
        new_node = Node(data)
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        print("new node added")
        tmp.next = new_node


n = Node(1)
l = LinkedList(n)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
l.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
l.print_linked_list()
l.add_node_at_tail(6)
l.print_linked_list()

n1 = Node(1)
tmp = n1
n2 = Node(2)
tmp.next = n2
tmp = n2
n3 = Node(3)
tmp.next = n3

nodes = [1, 2, 3, 4, 5]
print("-----------------")
for i in range(len(nodes)):
    node = Node(nodes[i])
    tmp = node
    tmp.next
    if i != 0:
        tmp.next = node
        tmp=Node(nodes[i])
    print(tmp.data, "->", tmp.next)

