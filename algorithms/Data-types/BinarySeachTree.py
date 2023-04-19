class BinarySeachTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            # Add in left side
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySeachTree(data)
        else:
            # Add in left side
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySeachTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self, val):
        if self.data == val:
            return True
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        elif val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

# root = BinarySeachTree(10)
# root.add_child(9)
# root.add_child(11)
# print(root)
# root.add_child(8)
# root.add_child(7)
# root.add_child(15)
# p


def build_tree(numbers):
    root = BinarySeachTree(10)
    for num in numbers:
        root.add_child(num)
    print(root.in_order_traversal())
    print(root.search(19))
    print(root.search(10))
    print(root.search(15))


build_tree([17, 11, 9, 8, 7, 15, 16, 18, 6, 5, 2, 11])
