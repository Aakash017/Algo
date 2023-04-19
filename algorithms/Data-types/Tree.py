"""
Tree data structure is used to represent hierarchical data such as organization hierachy, product categories,
geographic locations etc

"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        print('  ' + '|__' * self.get_level() + self.data) if self.parent else print(self.data)
        for child in self.children:
            child.print_tree()


root = TreeNode("Electronics")
t1 = TreeNode("Mobile")
t1.add_child(TreeNode("Iphone"))
t1.add_child(TreeNode("Samsung"))
t1.add_child(TreeNode("Nokia"))
t1.add_child(TreeNode("Redmi"))

t2 = TreeNode("Laptop")
t2.add_child(TreeNode("Mac"))
t2.add_child(TreeNode("HP"))
t2.add_child(TreeNode("Dell"))
t2.add_child(TreeNode("Lenovo"))

t3 = TreeNode("TV")
t3.add_child(TreeNode("Samsung"))
t3.add_child(TreeNode("LG"))

root.add_child(t1)
root.add_child(t2)
root.add_child(t3)

root.print_tree()