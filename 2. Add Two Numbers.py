# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            carry = 1 if carry >= 10 else 0
            cur = cur.next

        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next

a = Solution()
a.addTwoNumbers([1,2,3],[2,3,4])
