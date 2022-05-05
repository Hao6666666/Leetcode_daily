# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque([])
        cur = head
        while cur:
            q.append(cur)  ## 注意！！
            cur = cur.next

        dummy = ListNode(0)
        cur = dummy
        even = True
        while q:
            node = q.popleft() if even else q.pop()
            node.next = None  ### 注意！！
            cur.next = node
            even ^= True  ## XOR operater
            cur = cur.next
        return head
