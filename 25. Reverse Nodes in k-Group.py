# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 判断是否可以反转
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next

        # 反转
        prev = None
        cur = head
        for _ in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # 把新的head传进主函数
        head.next = self.reverseKGroup(cur, k)

        # 返回prev！！！！
        return prev
