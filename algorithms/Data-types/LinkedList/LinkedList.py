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


# n = Node(1)
# l = LinkedList(n)
# second_node = Node(2)
# third_node = Node(3)
# fourth_node = Node(4)
# fifth_node = Node(5)
# l.head.next = second_node
# second_node.next = third_node
# third_node.next = fourth_node
# fourth_node.next = fifth_node
# l.print_linked_list()
# l.add_node_at_tail(6)
# l.print_linked_list()
#
# n1 = Node(1)
# tmp = n1
# n2 = Node(2)
# tmp.next = n2
# tmp = n2
# n3 = Node(3)
# tmp.next = n3
#
# nodes = [1, 2, 3, 4, 5]
# print("-----------------")
# for i in range(len(nodes)):
#     node = Node(nodes[i])
#     tmp = node
#     tmp.next
#     if i != 0:
#         tmp.next = node
#         tmp = Node(nodes[i])
#     print(tmp.data, "->", tmp.next)


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def print_linked_list(self):
        print("printing Linked List \n")
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next

    def add_node_at_last(self, node):
        tmp = self.head
        while tmp.next:
            print(tmp.val)
            tmp = tmp.next
        tmp.next = node

    def add_node_at_start(self, node):
        tmp = self.head
        node.next = tmp
        self.head = node

    def add_node_at_after_given_node(self, node, prev_node):
        node.next = prev_node.next
        prev_node.next = node

    def get(self, index):
        count = 0
        tmp = self.head
        while count < index + 1:
            if count == index:
                return tmp
            else:
                count += 1
                tmp = tmp.next

    def set(self, index, value):
        tmp = self.get(index)
        tmp.val = value

    def pop_first(self):
        tmp = self.head
        self.head = tmp.next
        return tmp

    def pop(self):
        tmp = self.head
        while tmp.next.next:
            tmp = tmp.next
        pop_node = tmp.next
        tmp.next = None
        return pop_node

    def remove(self, index):
        tmp = self.get(index)
        pre_node = self.get(index - 1)
        pre_node.next = tmp.next
        return tmp

    def delete_all(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove_duplicates(self):
        # TODO
        seen = {}
        tmp = self.head
        seen[tmp.val] = 1
        while tmp.next is not None:
            prev = tmp
            next = tmp.next
            print(seen)
            if next.val in seen:
                prev.next = next.next
            else:
                seen[next.val] = 1
                # seen[next.value]=1
                tmp = tmp.next

    def return_from_last(self, n):
        '''
        Take two pointers with gap=n and move them when 2nd will be on last 1st will be on nth
        '''
        pointer1 = self.head
        pointer2 = self.head
        for i in range(n):
            if pointer2 is None:
                return None
            pointer2 = pointer2.next
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1.val

    def partition(self, x):
        """
        Partition Linked List such as all elements less than z will be on right side and all elemts greater
         than x will be on left side
        """
        left_ll = LinkedList(None)
        right_ll = LinkedList(None)
        tmp = self.head
        while tmp:
            if tmp.val < x:
                tmpnode = Node(tmp.val)
                tmpnode.next = left_ll.head
                left_ll.head = tmpnode
            else:
                tmpnode = Node(tmp.val)
                tmpnode.next = right_ll.head
                right_ll.head = tmpnode
            tmp = tmp.next
        l = left_ll.head
        while l.next:
            l = l.next
        l.next = right_ll.head
        left_ll.print_linked_list()
        return left_ll


l1 = Node(3)
l = LinkedList(l1)
l2 = Node(4)
l1.next = l2
l3 = Node(5)
l2.next = l3
l4 = Node(5)
l3.next = l4
l5 = Node(9)
l4.next = l5
l6 = Node(9)
l5.next = l6

# l.print_linked_list()
new_node = Node(10)
l.add_node_at_last(new_node)
# l.print_linked_list()

l.add_node_at_start(Node(1))

# l.print_linked_list()

l.add_node_at_after_given_node(Node(8), l6)

l.print_linked_list()

print(l.get(3))
# d = l.get(3)
# print(d.val)

l.set(6, 8)
l.set(7, 9)
l.set(8, 11)
# l.pop_first()
l.print_linked_list()
# d = l.pop_first()
# print(d.val)

# c=l.pop()
# print("poped", c.val)
# l.remove(3)

# l.print_linked_list()

# l.delete_all()
# l.print_linked_list()

# print("reverse...")
# l.reverse()
# print("reverse complete")

# l.print_linked_list()
# l.remove_duplicates()
# l.print_linked_list()

print("return fom last")
# print(l.return_from_last(1))
print("after partition")
result = l.partition(5)
result.print_linked_list()


# l.print_linked_list()

# Normal List Partition

# d = [1, 4, 5, 3, 6, 2]
# l = 0
# r = len(d) - 1
# for i in range(len(d)):
#     print(d[i], "d")
#     if d[i] <= 3:
#         d.insert(l, d.pop(i))
#         l += 1
#     else:
#         d.insert(r, d.pop(i))
#         r -= 1
# print(d)


def add_two_linkedlist(l1, l2):
    pass


l1 = Node(5)
l2 = l1
print(l1 == l2)

l1 = [2, 3, 4, 5]
l2 = [1, 7, 2]
