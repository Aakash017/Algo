"""
Stack of plates
"""


class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    # def push(self, item):
    #     if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
    #         self.stacks[-1].append(item)
    #     else:
    #         self.stacks.append(item)
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stacknum):
        if len(self.stacks[stacknum]) > 0:
            return self.stacks[stacknum].pop()
        else:
            return None


custome = PlateStack(2)
custome.push(1)
print(custome.__str__())

custome.push(2)
custome.push(3)
print(custome.pop())
