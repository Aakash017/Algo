# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        sum = 0
        carry = 0
        dummynode = ListNode(val=0, next=None)
        while l1 or l2:
            sum += carry + l1.val + l2.val
            if sum > 9:
                val = sum % 10
                carry = sum // 10
            val = sum
            carry = 0
            dummynode.val = val
            dummynode = dummynode.next
            l1 = l1.next
            l2 = l2.next
        return dummynode

s=Solution()
s.addTwoNumbers([1,2,3],[3,22,1])





