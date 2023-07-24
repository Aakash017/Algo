# Describe how you will use single python list to implement three stacks
# Convert list into three stacks

class Multistack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custlist = [0] * (stacksize * self.numberstacks)
        self.size = [0] * self.numberstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.size[stacknum] == self.stacksize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.size[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.size[stacknum] - 1

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return False
        else:
            self.size[stacknum] += 1
            self.custlist[self.indexOfTop(stacknum)] = item
    def pop(self,item, stacknum):
        if self.isEmpty(stacknum):
            return False
        else:
            val=self.custlist[self.indexOfTop(stacknum)]
            self.custlist[self.indexOfTop(stacknum)]=0
            self.size[stacknum]-=1
            return val

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return False
        else:
            val = self.custlist[self.indexOfTop(stacknum)]
            return val



customestack=Multistack(6)
print(customestack.isFull(0))
print(customestack.isEmpty(1))
customestack.push(1,0)
customestack.push(2,0)
customestack.push(3,2)
print(customestack.peek(0))


